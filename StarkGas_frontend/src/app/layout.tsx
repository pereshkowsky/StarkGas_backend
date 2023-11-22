import type { Metadata } from "next"
import { inter } from "@/assets/fonts/fonts"
import "@/scss/global.scss"
import TanstackProvider from "@/components/Providers/TanstackProvider"
import Footer from "@/components/Footer/Footer"
import { Analytics } from "@vercel/analytics/react"

export const metadata: Metadata = {
  title: "StarkGas",
  description: "Starknet Gas Fee Prediction",
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <TanstackProvider>
        <body className={inter.className}>
          {children}
          <Footer />
          <Analytics />
        </body>
      </TanstackProvider>
    </html>
  )
}
