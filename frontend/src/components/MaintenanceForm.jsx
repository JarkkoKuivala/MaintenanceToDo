import { useState } from "react";
import useAction from "../hooks/useAction";


const MaintenanceForm = () => {
    
    const [state,setState] = useState({
        maintenance:"",
        machine:"",
        deadline:""
    })


    const {add} = useAction();

    const onChange = (event) => {
        setState((state) => {
            return {
                ...state,
                [event.target.name]:event.target.value
            }
        })
    }

const onSubmit = (event) => {
    event.preventDefault();
    let item = {
        ...state
    }
    add(item);
    setState({
        maintenance:"",
        machine:"",
        deadline:""
    })
}


    return(
        <div style={{
            "backgroundColor":"#DCEFFD",
            "margin":"auto",
            "width":"40%",
            "textAlign":"center"
        }}>
            <form className="m-3" onSubmit={onSubmit}>
                <div className="form-group">
                    <label className="form-label" htmlFor="maintenance">Tehtävän nimi</label>
                    <input type="text"
                        name="maintenance"
                        id="maintenance"
                        className="form-control"
                        onChange={onChange}
                        value={state.maintenance}/>
                </div>
                <div className="form-group">
                    <label className="form-label" htmlFor="machine">Laite</label>
                    <input type="text"
                        name="machine"
                        id="machine"
                        className="form-control"
                        onChange={onChange}
                        value={state.machine}/>
                </div>
                <div className="form-group">
                    <label className="form-label" htmlFor="deadline">Tehtävän päivämäärä</label>
                    <input type="text"
                        name="deadline"
                        id="deadline"
                        className="form-control"
                        onChange={onChange}
                        value={state.deadline}/>
                </div>
                <input style={{"backgroundColor":"#124c81"}} type="submit" value="Lisää" className="btn btn-secondary"/>
            </form>
        </div>
    )

}







export default MaintenanceForm;