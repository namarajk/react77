import "./App.css";
import Home from "./components/home/Home";
import About from "./components/about/About";
import Services from "./components/services/Services";

import { Route, Routes } from "react-router-dom";

function App() {
  return (
    <div className="App">
      <Routes>
        <Route element={<Home />} path="/" />
        <Route element={<About />} path="/about" />
        <Route element={<Services />} path="/services" />
      </Routes>
    </div>
  );
}

export default App;
