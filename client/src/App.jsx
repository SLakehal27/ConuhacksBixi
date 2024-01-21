import "./App.css";
import "leaflet/dist/leaflet.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import MainPage from "./pages/MainPage.jsx";
import Header from "./components/Header";
import StatsPage from "./pages/StatsPage.jsx";
import Footer from "./components/Footer.jsx";

export default function App() {
  return (
    <>
      <Header />
      <BrowserRouter>
        <Routes>
          <Route default path="/" element={<MainPage />} />
          <Route path="/stats" element={<StatsPage />} />
        </Routes>
      </BrowserRouter>
      <Footer />
    </>
  );
}
