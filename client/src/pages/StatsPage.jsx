import React from "react";
import { Link } from "react-router-dom";
import { Container, Row, Col } from "react-bootstrap";
import { Graph } from "../consts/graphs";

export default function StatsPage() {
  const graph = new Graph();
  return (
    <div className="StatsPage">
      <Container>
        <Row>
          <Col>
            <h1>Statistiques et graphes</h1>
            {graph.render()}
          </Col>
        </Row>
        <Graph />
        <Row>
          <Col>
            <Link to="/">Retour</Link>
          </Col>
        </Row>
      </Container>
    </div>
  );
}
