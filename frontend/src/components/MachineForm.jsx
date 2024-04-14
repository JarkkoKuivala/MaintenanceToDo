import { useState } from "react";

const MachineForm = () => {
    
    return(
        <div style={{
            "backgroundColor":"#DCEFFD",
            "margin":"auto",
            "width":"40%",
            "textAlign":"center"
        }}>
            <form className="m-3" onSubmit={onSubmit}>
                <div className="form-group">
                    <label className="form-label" htmlFor="machine">Laitteen merkki</label>
                    <input type="text"
                        name="machine"
                        id="machine"
                        className="form-control"
                        onChange={onChange}
                        value={state.machine}/>
                </div>
                <div className="form-group">
                    <label className="form-label" htmlFor="model">Laitteen malli</label>
                    <input type="text"
                        name="model"
                        id="model"
                        className="form-control"
                        onChange={onChange}
                        value={state.model}/>
                </div>
                <input style={{"backgroundColor":"#124c81"}} type="submit" value="Lisää" className="btn btn-secondary"/>
            </form>
        </div>
    )

}

export default MachineForm;