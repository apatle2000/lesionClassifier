import "./styleSheets/App.css";
import AppContext from "./Context/Appcontext";

function App() {
  return (
      <AppContext.Provider value={{}}>
      <span>Hello</span>
      </AppContext.Provider>
  );
}

export default App;
