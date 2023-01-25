
import React, {useState, useEffect} from 'react'
import APIService from '../APIService';
import { useCookies } from 'react-cookie';


function Form(props) {
    const [title, setTitle] = useState(props.article.title)
    const [description, setDecsription] = useState('')
    const [token] = useCookies(['mytoken'])
    
    useEffect(() => {
        setTitle(props.article.title)
        setDecsription(props.article.description)
    }, [props.article])

    const updateArticle = () =>{
        APIService.UpdateArticle(props.article.id, {title, description}, token['mytoken'])
        .then(resp => props.updatedInformation(resp))
    }

    const insertArticle = () => {
        APIService.insertArticle({title, description}, token['mytoken'])
        .then(resp => props.insertedInformation(resp))
    }
  
    return (
    <div>
        {props.article ? (

            <div className='mb-3'>
            <label htmlFor='title' className='form-label'>Title</label>
            <input type='text' className='form-control' id='title' placeholder='please enter the title'
            value={title} onChange={e => setTitle(e.target.value)}
            />

            <label htmlFor='description' className='form-label'>Description</label>
            <textarea className='form-control' id='description' rows='5' placeholder='please enter the description'
            value={description} onChange={e => setDecsription(e.target.value)}
            />
            <br/>

            {
                props.article.id ? <button onClick={updateArticle} className='btn btn-success'>Update</button>
                : <button onClick={insertArticle} className='btn btn-success'>Insert Article</button>
            }
            
            
            </div>

        ) : null}

    </div>
  )
}

export default Form