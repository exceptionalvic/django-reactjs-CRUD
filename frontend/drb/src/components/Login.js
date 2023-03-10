

import React, {useState, useEffect} from 'react'
import APIService from '../APIService';
import { useCookies } from 'react-cookie';
import {useNavigate, useNavigation} from 'react-router-dom';
// import {useHistory} from 'react-router-dom'; //react-router-dom version <6

function Login() {

    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const [token, setToken] = useCookies(['mytoken'])

    const [isLogin, setLogin] =  useState(true)

    let navigation = useNavigate();
    // let history = useHistory();

    useEffect(() => {
        if(token['mytoken']){
            navigation('/articles')
            // history.push('/articles')
        }
    }, [token])

    const loginBtn = () => {
        APIService.LoginUser({username, password})
        .then(resp => setToken('mytoken', resp.token))
        .catch(error => console.log(error))
    }

    const registerBtn = () => {
        APIService.RegisterUser({username,password})
        .then(resp => loginBtn())
        .catch(error => console.log(error))
    }

  return (
    <div className='App'>
        <br/>
        <br/>
        {isLogin ? <h1>Please Login</h1> : <h1>Please Register</h1>}
        
        <br/>
        <br/>
        <div className='mb-3'>

            <label htmlFor='username' className='form-label'>username</label>
            <input type='text' className='form-control' id='username' placeholder='please enter username'
            value={username} onChange={e => setUsername(e.target.value)}
            />

        </div>
        <div className='mb-3'>

            <label htmlFor='password' className='form-label'>password</label>
            <input type='password' className='form-control' id='password' placeholder='please enter password'
            value={password} onChange={e => setPassword(e.target.value)}
            />

        </div>
        {isLogin ? <button onClick={loginBtn} className='btn btn-primary'>Login</button> : <button onClick={registerBtn} className='btn btn-primary'>Register</button>}

        <div className='mb-3'>
        <br/>
        {isLogin ? <h5>If you don't have account, please <button className='btn btn-primary btn-sm' onClick={()=> setLogin(false)}>Register</button> here</h5>
            :<h5>If you have an account, please<button className='btn btn-primary btn-sm' onClick={()=> setLogin(true)}>Login</button> Here</h5>
        }

        </div>
    </div>
  )
}

export default Login