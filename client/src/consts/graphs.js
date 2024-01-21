import React, { useEffect, useState } from "react";
import { Bar } from "react-chartjs-2";
import { SERVER_URL } from "./consts";
import {
  Chart as ChartJS,
  BarElement,
  CategoryScale,
  LinearScale,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(BarElement, CategoryScale, LinearScale, Tooltip, Legend);

export function Graph() {
  const [data, setData] = useState([]);

  useEffect(() => {
    async function loadData() {
      try {
        const res = await fetch(`${SERVER_URL}/data`);
        const jsonData = await res.json();
        setData(jsonData); // Mise à jour de l'état avec les données
      } catch (error) {
        console.error("Error fetching data: ", error);
      }
    }

    loadData();
  }, []);

  const sortedData = [...data].sort((a, b) => b.visit_count - a.visit_count);

  const labels = sortedData.map((d) => d.address);

  // Assigner une couleur en fonction de l'achalandage
  const backgroundColor = sortedData.map((d) => {
    switch (
      d.type // Remplacez 'achalandage' par le nom réel de votre propriété
    ) {
      case "high":
        return "green";
      case "average":
        return "orange";
      case "low":
        return "red";
      default:
        return "green";
    }
  });

  const datasets = [
    {
      label: "Visit Count",
      data: sortedData.map((d) => d.visit_count),
      backgroundColor, // Utilisation du tableau de couleurs
    },
  ];

  const chartData = {
    labels,
    datasets,
  };

  return (
    <div>
      <Bar data={chartData} />
    </div>
  );
}
