import Hero from '@/components/Pages/Home/Hero'
import React from 'react'
import Navbar from '@/components/Constants/Navbar'
import Footer from '@/components/Constants/Footer'

type Props = {}

export default function page({}: Props) {
  return (
    <div>
      <Navbar />
      <Hero />
      <Footer />

    </div>
  )
}