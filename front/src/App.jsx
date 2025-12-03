import React from 'react'
import { useState,useEffect } from 'react'

const App = () => {
  const [btn , setBtn] = useState('Click Me')
  const [data, setData] = useState(null)
  const [hours, setHours] = useState("1")
  const fetchData = ()=>{
    fetch(`http://127.0.0.1:5000/?hours=${hours}`)
    .then(res => res.json())
    .then(data => {
      console.log(data);
      setData(data)
      setBtn('Data Fetched')
    })
    .catch(err => {
      console.error("Error fetching data:", err);
      setBtn('Error Fetching Data')
    });

  }
  useEffect(()=>{
    fetchData()
  },[])
  return (
    <div>
      <form>
        <label htmlFor="inputField">Enter Hour: </label>
        <input type="text" placeholder='Enter Something' value={hours} onChange={(e)=>setHours(e.target.value)}/>
      </form>
      <button type="submit" onClick={fetchData}>{btn}</button>
      {data && <div>
        <h3>Predicted Score: {data.data}</h3>
        <img src={`http://127.0.0.1:5000/${data.graph_url}`}  style={{maxWidth:"400px"}}/>
      </div>}
    </div>
  )
}

export default App