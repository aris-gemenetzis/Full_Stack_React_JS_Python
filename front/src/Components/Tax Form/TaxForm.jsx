import React from 'react'
import { useState } from "react";
import './TaxForm.css'
import axios from 'axios'

const TaxForm = () => {

  const [inputs, setInputs] = useState({});

    async function getData() {
      try {
        const response = await axios.get('http://localhost:8000/forms');
        console.log(response.data);
      } catch (error) {
        console.error(error);
      }
    }

    async function updateForm(event) {
      event.preventDefault();
      console.log(inputs);
      const newForm = {
        company: inputs.company,
        revenue: inputs.revenue,
        costs: inputs.costs,
        id: count-1,
      }
      try {
        const response = await axios.put('http://localhost:8000/forms/'+(count-1), newForm);
        console.log(response.data);
      } catch (error) {
        console.error(error);
      }
    }

    async function postForm(event) {
      event.preventDefault();
      increment();
      console.log(inputs);
      const newForm = {
        company: inputs.company,
        revenue: inputs.revenue,
        costs: inputs.costs,
        id: count,
      }
      try {
        const response = await axios.post('http://localhost:8000/forms/add', newForm);
        console.log(response.data);
      } catch (error) {
        console.error(error);
      }
    }

    const handleClick = () => {
      decrement()
      axios.delete('http://localhost:8000/forms/'+(count-1));
  }

  const handleChange = (event) => {
    const name = event.target.name;
    const value = event.target.value;
    setInputs(values => ({...values, [name]: value}))
  }

  const [count, setCount] = useState(1); 

  function increment() {
    setCount(count + 1);
  };

  function decrement() {
    setCount(count - 1);
  };

  return (
    <div className='container'>
        <div className='header'>
            <div className='text'>Tax Form</div>
            <div className='underline'> </div>
        </div>
        <div className='inputs'>
            <form>
                <div className='form-table'>
                    <label htmlFor='company'>Company name</label>
                    <input type='text' id='company' name='company' 
                    value={inputs.company || ""} 
                    onChange={handleChange}/>
                </div>
                <div className='form-table'>
                    <label htmlFor='revenue'>Revenue</label>
                    <input type='number' id='revenue' name='revenue' 
                    value={inputs.revenue || ""} 
                    onChange={handleChange}/>
                </div>
                <div className='form-table'>
                    <label htmlFor='costs'>Costs</label>
                    <input type='number' id='costs' name='costs' 
                    value={inputs.costs || ""} 
                    onChange={handleChange}/>
                </div>
            </form>
        </div>
        <div className='button-container'>
        <noscript className="comment">axios get tester button</noscript>
          <div className='button' onClick={getData}>Get
          </div>
          <noscript className="comment">axios put tester button</noscript>
          <div className='button' onClick={updateForm}>Update
          </div>
          <noscript className="comment">axios delete tester button</noscript>
          <div className='button' onClick={handleClick}>Delete
          </div>
          <noscript className="comment">axios post tester button</noscript>
          <div className='button' onClick={postForm}>Submit
          </div>
        </div>
        <div className='test-container'>
          <div className='response'>
          </div>
        </div>
    </div>
  )
}

export default TaxForm
