import { Link } from "react-router-dom";

const Navbar = (props) => {

    return(
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
                <p className="navbar-brand" style={{marginLeft:20}}>Maintenance ToDo App</p>
                <ul className="navbar-nav">
                    <li className="nav-item" style={{marginLeft:20}}>
                        <Link to="/" className="nav-link">ToDo Listaus</Link>
                    </li>
                    <li className="nav-item" style={{marginLeft:20}}>
                        <Link to="/maintenanceform" className="nav-link">Lisää uusi huolto</Link>
                    </li>
                    <li className="nav-item" style={{marginLeft:20}}>
                        <Link to="/machineform" className="nav-link">Lisää uusi laite</Link>
                    </li>
                    <li className="nav-item" style={{marginLeft:20}}>
                        <Link to="/done" className="nav-link">Tehdyt huollot</Link>
                    </li>
                </ul>
        </nav>
        
    )
}

export default Navbar;