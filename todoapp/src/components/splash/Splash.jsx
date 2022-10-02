import React from 'react';

import './Splash.css'
import logo from '../../assets/icons/icon.svg';

function Splash() {
    return (
        <div className="splash-container">
            <div className="splash"></div>
            <div className="logo">
                <img src={logo} alt="logo" />
            </div>
        </div>
    );
}

export default Splash;