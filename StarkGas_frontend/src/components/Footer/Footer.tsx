import SVGIcon from "@/assets/icons/SVGIcon"
import styles from "./Footer.module.scss"
import Link from "next/link"

const Footer = () => {
  return (
    <div className={styles.container}>
      <div>
        <p className={styles.made}>
          <SVGIcon name="logo" /> Made by PERESHKOWSKY
        </p>
        <Link href={"https://t.me/dondo_di_danda"}>
          <p className={styles.tg}>my Telegram</p>
        </Link>
      </div>
      <p>0x062C3e58C55428602Cc771a942e9a8e9A884C04f048fAfC768971b59bc26a0D3 ♡</p>
    </div>
  )
}

export default Footer
