import React, { Component } from "react";
import { Line } from "react-chartjs-2";
import { SERVER_URL } from "./consts";

export class Graph extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
    };
  }

  componentDidMount() {
    this.loadData();
  }

  async loadData() {
    try {
      const res = await fetch(`${SERVER_URL}/data`);
      const data = await res.json();
      this.setState({ data });
    } catch (error) {
      console.error("Error fetching data: ", error);
    }
  }

  render() {
    const { data } = this.state;
    const labels = data.map((d) => d.date);
    const datasets = [
      {
        label: "Address",
        data: data.map((d) => d.address),
        borderColor: "red",
      },
      {
        label: "Latitude",
        data: data.map((d) => d.latitude),
        borderColor: "blue",
      },
      {
        label: "Longitude",
        data: data.map((d) => d.longitude),
        borderColor: "green",
      },
      {
        label: "Type",
        data: data.map((d) => d.type),
        borderColor: "yellow",
      },
    ];
    const chartData = {
      labels,
      datasets,
    };

    return (
      <div>
        <Line data={chartData} />
      </div>
    );
  }
}
