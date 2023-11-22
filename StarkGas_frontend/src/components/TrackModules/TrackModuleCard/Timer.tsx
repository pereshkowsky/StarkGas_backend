"use client";

import { useEffect, useState } from "react";

const Timer = ({ gas_time }: { gas_time: number }) => {
  const [now, setNow] = useState<number>(
    Math.round(Date.now() / 1000 - gas_time)
  );
  useEffect(() => {
    setNow(Math.round(Date.now() / 1000 - gas_time));
    const i = setInterval(() => {
      setNow((prev) => prev + 1);
    }, 1000);
    return () => {
      clearInterval(i);
    };
  }, [gas_time]);
  return (
    <>
      {now > 60
        ? `${Math.floor(now / 60)}m ${now - 60 * Math.floor(now / 60)}s`
        : `${now}s`}
    </>
  );
};

export default Timer;
