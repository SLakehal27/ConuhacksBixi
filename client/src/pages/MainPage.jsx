import React, { useRef, useEffect, useState } from "react";
import { MapContainer, Marker, TileLayer, useMapEvents } from "react-leaflet";
import { useNavigate } from "react-router-dom";
import { SERVER_URL } from "../consts/consts";
import {
  highMarker,
  lowMarker,
  averageMarker,
  currentMarker,
} from "../consts/markers";
import L from "leaflet";

export default function MainPage() {
  const navigate = useNavigate();
  const [high, setHigh] = useState([]);
  const [average, setAverage] = useState([]);
  const [low, setLow] = useState([]);
  const [isVisible, setVisible] = useState(true);
  const [map, setMap] = useState(null);
  const mapRef = useRef(null);

  useEffect(() => {
    async function getHighStations() {
      try {
        const response = await fetch(`${SERVER_URL}/bixi/high`);
        if (!response.ok) {
          setHigh([]);
          return;
        }
        const data = await response.json();
        setHigh(data);
      } catch {
        setHigh([]);
      }
    }

    async function getAverageStations() {
      try {
        const response = await fetch(`${SERVER_URL}/bixi/average`);
        if (!response.ok) {
          setAverage([]);
          return;
        }
        const data = await response.json();
        setAverage(data);
      } catch {
        setAverage([]);
      }
    }

    async function getLowStations() {
      try {
        const response = await fetch(`${SERVER_URL}/bixi/low`);
        if (!response.ok) {
          setLow([]);
          return;
        }
        const data = await response.json();
        setLow(data);
      } catch {
        setLow([]);
      }
    }

    getHighStations();
    getAverageStations();
    getLowStations();

    if (mapRef.current) {
      const map = mapRef.current;
      const rectangleBounds = [
        [45.506, -73.556],
        [45.509, -73.552],
      ];
      map.fitBounds(rectangleBounds);

      setMap(map);
    }
  }, []);

  function MapLocator() {
    const map = useMapEvents({
      click: (e) => {
        if (map) {
          console.log(e.latlng);
          L.marker(e.latlng, { icon: currentMarker }).addTo(map);
        }
      },
    });
    return null;
  }

  return (
    <>
      <div style={{ width: "100%", maxWidth: "600px", margin: "0 auto" }}>
        <MapContainer
          className="mt-8 border-2 border-black rounded-md "
          center={[45.4958, -73.579]}
          zoom={21}
          style={{ height: "400px" }}
          whenCreated={(map) => (mapRef.current = map)}
        >
          <MapLocator />
          <TileLayer
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            attribution="© OpenStreetMap contributors"
          />

          {high.map((station, index) => {
            return (
              isVisible && (
                <Marker
                  className=""
                  key={index}
                  position={[station.latitude, station.longitude]}
                  icon={highMarker}
                />
              )
            );
          })}

          {average.map((station, index) => {
            return (
              isVisible && (
                <Marker
                  key={index}
                  position={[station.latitude, station.longitude]}
                  icon={averageMarker}
                />
              )
            );
          })}
          {low.map((station, index) => {
            return (
              isVisible && (
                <Marker
                  className="hidden"
                  key={index}
                  position={[station.latitude, station.longitude]}
                  icon={lowMarker}
                />
              )
            );
          })}
        </MapContainer>

        {/* Add useMapEvents for click handling */}

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
