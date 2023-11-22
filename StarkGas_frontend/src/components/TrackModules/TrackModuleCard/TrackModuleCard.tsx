import Image from "next/image"
import { TrackModule } from "../TrackModules"
import styles from "./TrackModuleCard.module.scss"
import Timer from "./Timer"
import Link from "next/link"

const TrackModuleCard = ({
  module_name,
  name,
  description,
  with_approve,
  gas_eth,
  gas_usd,
  gas_time,
  url,
}: TrackModule) => {
  return (
    <div className={styles.container} key={module_name}>
      {url ? (
        <Link href={url}>
          <div className={styles.logo_wrapper}>
            <Image src={`/imgs/logos/${name.toLowerCase()}.png`} fill alt={`${name} logo`} />
          </div>
        </Link>
      ) : (
        <div className={styles.logo_wrapper}>
          <Image src={`/imgs/logos/${name.toLowerCase()}.png`} fill alt={`${name} logo`} />
        </div>
      )}

      <div className={styles.header}>
        {url ? (
          <Link href={url} target="_blank">
            <div className={styles.name}>{name}</div>
          </Link>
        ) : (
          <div className={styles.name}>{name}</div>
        )}

        <div className={styles.description}>{description}</div>
      </div>

      <div className={styles.content}>
        <div className={styles.description}>
          gas in eth
          {with_approve && <div className={`${styles.description} ${styles.approve}`}>+a</div>}
        </div>
        <div className={styles.value}>{`${gas_eth} eth`}</div>
      </div>

      <div className={styles.content}>
        <div className={styles.description}>
          gas in usd
          {with_approve && <div className={`${styles.description} ${styles.approve}`}>+a</div>}
        </div>
        <div className={styles.value}>{`${gas_usd}$`}</div>
      </div>

      <div className={styles.content}>
        <div className={styles.description}>last update</div>

        <div className={styles.value}>
          <Timer gas_time={gas_time} /> ago
        </div>
      </div>
    </div>
  )
}

export default TrackModuleCard
