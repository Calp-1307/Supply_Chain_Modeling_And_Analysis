# Facility Location and Network Design Models

## Overview

This repository contains a collection of classical **Facility Location** and **Network Design** optimization models developed as instructional material for **ISE 453 – Modeling and Analysis of Supply Chains** at **North Carolina State University**, where I served as the course instructor.

The objective of this repository is to demonstrate how mathematical optimization techniques can be used to support strategic supply chain decisions, including facility placement, service coverage, customer assignment, transportation planning, and network design.

The models are implemented in Python using industry-standard optimization tools such as **Gurobi** and **Pyomo**, with solutions obtained through commercial and open-source optimization solvers.

---

## Learning Objectives

The models included in this repository are designed to help students and practitioners understand how Operations Research techniques can be applied to real-world supply chain problems.

Topics covered include:

* Facility location decisions
* Customer-to-facility assignment
* Service coverage analysis
* Capacity planning
* Transportation network optimization
* Geographic distance modeling
* Multi-commodity flow optimization

---

## Models Included

### Set Covering Problem (SCP)

Determines the minimum number of facilities required to provide service coverage to all customers within a specified service distance or response threshold.

**Applications**

* Emergency services
* Healthcare facility placement
* Retail service coverage

---

### Maximal Covering Location Problem (MCLP)

Selects a limited number of facilities to maximize the amount of customer demand covered.

**Applications**

* Ambulance deployment
* Fire station placement
* Public service planning

---

### P-Median Problem

Determines the optimal locations of a fixed number of facilities while minimizing the total weighted distance between customers and facilities.

**Applications**

* Warehouse location
* Distribution center planning
* Logistics network design

---

### Uncapacitated Facility Location Problem (UFLP)

Determines which facilities should be opened while minimizing fixed facility costs and transportation costs.

**Applications**

* Strategic supply chain design
* Warehouse placement
* Distribution network optimization

---

### Capacitated Facility Location Problem (CFLP)

Extends the facility location problem by incorporating capacity limitations at facilities.

**Applications**

* Manufacturing networks
* Distribution systems
* Capacity planning

---

### 2D Mini-Sum Location Problem

Determines the location of a facility that minimizes the total rectilinear distance to all demand points.

---

### Weighted 2D Mini-Sum Location Problem

Extends the Mini-Sum model by incorporating customer demand weights.

**Applications**

* Urban logistics
* Distribution center placement
* Service network planning

---

### Great Circle Distance Calculations

Implements spherical distance calculations used in geographically distributed supply chain networks.

**Applications**

* National distribution networks
* International logistics
* Transportation planning

---

### Multi-Commodity Network Design Problem

Determines the optimal flow of multiple products through a transportation network while minimizing total system costs.

The model considers:

* Multiple commodities
* Transportation costs
* Network capacities
* Flow conservation constraints

**Applications**

* Supply chain network optimization
* Freight transportation planning
* Manufacturing-distribution systems

---

## Software and Tools

* Python
* Gurobi Optimizer
* Pyomo
* HiGHS Solver
* Mathematical Programming
* Mixed Integer Linear Programming (MILP)

---

## Educational Context

These models were developed as part of the teaching material for **ISE 453 – Modeling and Analysis of Supply Chains** at North Carolina State University.

The repository is intended to provide students, researchers, and practitioners with practical implementations of foundational supply chain optimization models while demonstrating how Operations Research methods can be applied to support strategic decision-making.

---

## Future Additions

This repository will continue to expand with additional supply chain optimization topics, including:

### Inventory Models

* Economic Order Quantity (EOQ)
* Newsvendor Models
* Multi-Period Inventory Planning
* Safety Stock Optimization

### Vehicle Routing Models

* Traveling Salesman Problem (TSP)
* Capacitated Vehicle Routing Problem (CVRP)
* Vehicle Routing Problem with Time Windows (VRPTW)

### Additional Case Studies

Realistic supply chain case studies designed to integrate multiple optimization techniques and support managerial decision-making.

---

## Author

**Carlos Alfredo Leca Pérez, Ph.D.**

Industrial and Systems Engineer

Research Interests:

* Supply Chain Optimization
* Facility Location
* Network Design
* Operations Research
* Mathematical Programming
* Data Analytics
* Decentralized Resource Allocation

GitHub: https://github.com/Calp-1307
