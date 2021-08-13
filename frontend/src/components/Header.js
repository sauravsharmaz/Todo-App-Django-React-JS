import React from 'react'
import {Link} from 'react-router-dom'

function Header() {
    return (
        <div className="header-container">
            <div className="header">
                <Link to='/'>
                    <div className="title">TODO APP</div>
                </Link>
            </div>
        </div>
    )
}

export default Header
