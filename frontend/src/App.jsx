import Navbar from './components/Navbar';
import MaintenanceList from './components/MaintenanceList';
import MaintenanceForm from './components/MaintenanceForm';
import MachineForm from './components/MachineForm';
//import ShoppingList from './components/ShoppingList';
import {Routes,Route,Navigate} from 'react-router-dom';

function App() {


  return (
    <>
      <Navbar/>
      <Routes>
        <Route path="/" element={<MaintenanceList/>}/>
        <Route path="/machineform" element={<MachineForm/>}/>
				<Route path="/maintenanceform" element={<MaintenanceForm/>}/>
        <Route path="*" element={<Navigate to="/"/>}/>
			</Routes>
    </>
  )
}

export default App;
