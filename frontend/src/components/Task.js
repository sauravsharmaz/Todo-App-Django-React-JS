import React from 'react'
import {Link} from 'react-router-dom'

function Task({task}) { 
    return ( 
        <div className="task-card">
            <div className="task-title">{task.title}</div>
            <div className="btns">
                <div className="delete">Delete</div>
                <Link to='/edit'>
                    <div className="Edit">Edit</div>
                </Link>
            </div>
        </div> 
    )
}

export default Task
