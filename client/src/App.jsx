import logo from "./logo.svg";
import "./App.css";

import React, { useRef, useEffect } from "react";
import { MapContainer, TileLayer, Rectangle } from "react-leaflet";
import "leaflet/dist/leaflet.css";

const MontrealMap = () => {
  const mapRef = useRef(null);

  useEffect(() => {
    if (mapRef.current) {
      const map = mapRef.current;
      const rectangleBounds = [
        [45.506, -73.556],
        [45.509, -73.552],
      ];

      // Fit the map to the rectangle bounds
      map.fitBounds(rectangleBounds);
    }
  }, []);

  return (
    <>
      <h1>BixiFlow</h1>
      <div style={{ width: "100%", maxWidth: "600px", margin: "0 auto" }}>
        <MapContainer
          center={[45.5088, -73.554]}
          zoom={13}
          style={{ height: "300px" }}
          whenCreated={(map) => (mapRef.current = map)}
        >
          {/* Add OpenStreetMap tile layer */}
          <TileLayer
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            attribution="© OpenStreetMap contributors"
          />
        </MapContainer>
      </div>
      <p>
        © Selim Lakehal, Andreea Maria Ghioltan, Anastassiya Kim, Nacim Bourelam
      </p>
    </>
  );
};

export default MontrealMap;
