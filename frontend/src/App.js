import Header from "./components/Header";
import TaskList from './components/TaskList'
import EditSection from "./components/EditSection";
import {BrowserRouter,Route} from 'react-router-dom'


function App() {
  return (
    <div className="App"> 
      <BrowserRouter>
        <Header />  
          <Route path='/' component={TaskList} exact />
          <Route path='/edit' component={EditSection} exact />  
      </BrowserRouter>
    </div>
  );
}

export default App;
