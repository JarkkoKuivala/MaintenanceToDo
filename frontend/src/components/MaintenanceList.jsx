import { useState } from "react";
import Row from './Row';


const MaintenanceList = (props) => {

    

    

    return(
        <table className="table table-striped">
            <thead>
                <tr>
                    <th>Tehtävä</th>
                    <th>Deadline</th>
                    <th>Laite</th>
                </tr>
            </thead>
            <tbody>
                {items}
            </tbody>
        </table>
    )
}

export default MaintenanceList;