import L from "leaflet";
import high from "../assets/MarkerHigh.png";
import average from "../assets/MarkerAverage.png";
import low from "../assets/MarkerLow.png";

export const highMarker = L.icon({
  iconUrl: high,
  iconSize: [48, 48],
  iconAnchor: [22, 94],
  shadowAnchor: [4, 62],
  popupAnchor: [-3, -76],
});
export const averageMarker = L.icon({
  iconUrl: average,
  iconSize: [48, 48],
  iconAnchor: [22, 94],
  shadowAnchor: [4, 62],
  popupAnchor: [-3, -76],
});
export const lowMarker = L.icon({
  iconUrl: low,
  iconSize: [48, 48],
  iconAnchor: [22, 94],
  shadowAnchor: [4, 62],
  popupAnchor: [-3, -76],
});
