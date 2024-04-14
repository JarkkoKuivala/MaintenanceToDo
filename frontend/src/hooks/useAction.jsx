import { useState, useEffect, useContext} from "react";


const useAction = () => {

    const  [state,setState] = useState({
        list:[]
    })

    const [urlRequest,setUrlrequest] = useState({
        url:"",
        request:{},
        action:""
    })

    useEffect(() => {}, [urlRequest]);

    const getTodos = () => {
        setUrlrequest({
            url:"/api/todos"
        })
    }


   return {getTodos}
 
}

export default useAction;