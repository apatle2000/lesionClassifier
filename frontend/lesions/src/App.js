import "./styleSheets/App.css";
import AppContext from "./Context/Appcontext";
import { useEffect } from "react";

function App() {
  useEffect(() => {
    //api call to the backend server
    fetch("connections/ping", {
      method: "GET",
    });
  }, []); // will run only once when the component is rendered 
  return (
    <AppContext.Provider value={{}}>
      <span>Hello</span>
    </AppContext.Provider>
  );
}

export default App;
