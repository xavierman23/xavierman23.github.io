import logo from './logo.svg';
import React, { useState } from 'react';
import './App.css';

function App() {
  const [value, setValue] = useState('');
  return (
    <div className="page">
      <h1>cAIculator</h1>
      <div className="container">
        <div className="calculator">
          <form action="">
            <div className="display">
              <input type="text" value={value}/>
            </div>
            <div>
              <input type="button" value="CE" onClick={e => setValue('')}/>
              <input type="button" value="DE" onClick={e => {
                try {
                  setValue(value.slice(0,-1));
                } catch (error) {
                  setValue('');
                }
              }}/>
              <input type="button" value="(" onClick={e => setValue(value + e.target.value)}/>
              <input type="button" value=")" onClick={e => setValue(value + e.target.value)}/>
            </div>
            <div>
              <input type="button" value="7" onClick={e => setValue(value + e.target.value)}/>
              <input type="button" value="8" onClick={e => setValue(value + e.target.value)}/>
              <input type="button" value="9" onClick={e => setValue(value + e.target.value)}/>
              <input type="button" value="/" onClick={e => setValue(value + e.target.value)}/>
            </div>
            <div>
              <input type="button" value="4" onClick={e => setValue(value + e.target.value)}/>
              <input type="button" value="5" onClick={e => setValue(value + e.target.value)}/>
              <input type="button" value="6" onClick={e => setValue(value + e.target.value)}/>
              <input type="button" value="*" onClick={e => setValue(value + e.target.value)}/>
            </div>
            <div>
              <input type="button" value="3" onClick={e => setValue(value + e.target.value)}/>
              <input type="button" value="2" onClick={e => setValue(value + e.target.value)}/>
              <input type="button" value="1" onClick={e => setValue(value + e.target.value)}/>
              <input type="button" value="+" onClick={e => setValue(value + e.target.value)}/>
            </div>
            <div>
              <input type="button" value="0" onClick={e => setValue(value + e.target.value)}/>
              <input type="button" value="." onClick={e => setValue(value + e.target.value)}/>
              <input type="button" value="="  onClick={e => {
                try {
                  setValue(eval(value)); // must eval(string)
                } catch (error) {}
              }}/>
              <input type="button" value="-" onClick={e => setValue(value + e.target.value)}/>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}

export default App;
