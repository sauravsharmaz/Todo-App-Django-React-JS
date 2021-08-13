import React,{useState, useEffect} from 'react'
import axios from 'axios'   
import Task from './Task'

function TaskList() { 
    async function getAllTasks(url){
        let resp = await axios.get(url);  
        let all_tasks= await resp.data   
        return all_tasks;
    }
    const [allTasks, setAllTasks]= useState([])
    useEffect(()=>{
        async function appendTasks(){
            let alltasks= await getAllTasks('http://127.0.0.1:8000/api/retrieve')
            setAllTasks(alltasks)
        }
        appendTasks()
    })
    return (
        <div className="TaskList">
            {
                allTasks.map(function(task){ 
                    return( 
                        <Task task={task} /> 
                    )
                })
            }
        </div>
    )
}

export default TaskList
