import TrackModules from "@/components/TrackModules/TrackModules"
import styles from "./Home.module.scss"
import Header from "@/components/Header/Header"

export default function Home() {
  return (
    <>
      <Header />
      <main className={styles.main}>
        <TrackModules />
      </main>
    </>
  )
}
