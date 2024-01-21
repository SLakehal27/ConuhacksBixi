import React from "react";
import { Link } from "react-router-dom";
import { Container, Row, Col } from "react-bootstrap";
import { Graph } from "../consts/graphs";

export default function StatsPage() {
  return (
    <div className="StatsPage">
      <Container>
        <Row>
          <Col>
            <h1 className="text-center font-black mb-4 mt-4">
              Statistiques et graphes
            </h1>
          </Col>
        </Row>
        <Graph />
      </Container>
    </div>
  );
}
