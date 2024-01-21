import React, { useRef, useEffect } from "react";
import { MapContainer, TileLayer } from "react-leaflet";
import { useNavigate } from "react-router-dom";

export default function MainPage() {
  const navigate = useNavigate();
  const mapRef = useRef(null);

  useEffect(() => {
    if (mapRef.current) {
      const map = mapRef.current;
      const rectangleBounds = [
        [45.506, -73.556],
        [45.509, -73.552],
      ];
      map.fitBounds(rectangleBounds);
    }
  }, []);

  return (
    <>
      <div style={{ width: "100%", maxWidth: "600px", margin: "0 auto" }}>
        <MapContainer
          className="mt-8 border-2 border-black rounded-md "
          center={[45.5088, -73.554]}
          zoom={13}
          style={{ height: "400px" }}
          whenCreated={(map) => (mapRef.current = map)}
        >
          <TileLayer
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            attribution="© OpenStreetMap contributors"
          />
        </MapContainer>
        <div className="text-center">
          <button
            className="bg-green-300 rounded-md mt-6 p-4 hover:scale-110 transition"
            onClick={(e) => {
              navigate("/stats");
            }}
          >
            Stats for nerds
          </button>
        </div>
      </div>
    </>
  );
}
