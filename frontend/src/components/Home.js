import React from 'react'
import video from '../media/earth.mp4'
import './css/Home.css'
const Home = () => {
    return (
        <div className='home'>
            <video className='home-video' src={video} autoPlay muted loop></video>
            <div className='home-info'>
                <h3>Hi, I am Darko</h3>
                <p>Computer engineering and technology graduate offering a strong foundation in software
                    engineering and programming principles across multiple platforms. Experienced in objectoriented programming; developing; testing and debugging code; designing interfaces and
                    administering systems and networks. Quickly learn and master new technologies; successful
                    working in both team and self-directed settings.
                </p>
            </div>
        </div>
    )
}

export default Home
