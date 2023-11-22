import styles from "./Loading.module.scss";

const Loading = () => {
  return (
    <>
      <div className={styles.container} style={{ opacity: "50%" }}></div>
      <div className={styles.container} style={{ opacity: "40%" }}></div>
      <div className={styles.container} style={{ opacity: "30%" }}></div>
      <div className={styles.container} style={{ opacity: "20%" }}></div>
      <div className={styles.container} style={{ opacity: "10%" }}></div>
    </>
  );
};

export default Loading;
