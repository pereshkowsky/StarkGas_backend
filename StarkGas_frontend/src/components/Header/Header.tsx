"use client"

import { useQuery } from "@tanstack/react-query"
import axios from "axios"
import SVGIcon from "@/assets/icons/SVGIcon"
import styles from "./Header.module.scss"
import Link from "next/link"

interface Gas {
  name: string
  gwei: number
}

const Header = () => {
  const { data, isLoading, isError } = useQuery({
    queryKey: ["Gas"],
    queryFn: async () => {
      const { data } = await axios.get("https://stark-gas-back.vercel.app/API/GAS")
      return data as Gas[]
    },
    refetchInterval: 1000,
  })
  return (
    <div className={styles.header}>
      <Link href={"/"}>
        <div className={styles.logo_wrapper}>
          <SVGIcon name="logo" />
        </div>
      </Link>
      {data?.map((item) => (
        <div className={styles.monitors} key={item.name}>{`${item.name}: ${item.gwei} gwei`}</div>
      ))}
      <div></div>
      <div className={styles.soon}>
        Charts<span className={styles.tip}>soon</span>
      </div>
      <div className={styles.soon}>
        DEX Spreads<span className={styles.tip}>soon</span>
      </div>
      <div className={styles.soon}>
        Tools<span className={styles.tip}>soon</span>
      </div>
    </div>
  )
}

export default Header
