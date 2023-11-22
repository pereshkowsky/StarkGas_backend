"use client"

import { useQuery } from "@tanstack/react-query"
import axios from "axios"
import TrackModuleCard from "./TrackModuleCard/TrackModuleCard"
import Loading from "./Loading"

export interface TrackModule {
  module_name: string
  name: string
  description: string
  with_approve: boolean
  gas_eth: number
  gas_usd: number
  gas_time: number
  url: string
}

const TrackModules = () => {
  const { data, isLoading, isError } = useQuery({
    queryKey: ["TrackModules"],
    queryFn: async () => {
      const { data } = await axios.get("https://stark-gas-back.vercel.app/API/ALL")
      return data as TrackModule[]
    },
    refetchInterval: 1000,
  })

  if (isLoading) {
    return <Loading />
  }
  if (isError) {
    return <div>Error</div>
  }

  return (
    <>
      {data?.map((item) => (
        <TrackModuleCard {...item} />
      ))}
    </>
  )
}

export default TrackModules
