# Swarm-6G Mini Project

A Python-based mini project exploring how communication constraints affect coordination in a simple robot swarm.

This project was built to demonstrate practical interest in the PhD topic:

**Embodied Intelligence for 6G Enabled Robot Swarms**

---

## Project Overview

The project simulates a group of simple agents moving in a 2D environment. Agents explore the area, discover a target, and share information with nearby neighbours.

The key idea is to study how swarm behaviour changes when communication becomes unreliable.

The simulation includes:

- multi-agent movement in a 2D space
- local communication between nearby agents
- message delay (latency)
- packet loss
- target discovery and information spreading
- experiment comparison across network conditions
- visualisation of swarm behaviour and explored area

---

## Research Motivation

Future robot swarms in 6G-enabled environments are expected to rely on fast and reliable communication for coordination, sensing, and distributed decision-making.

This project explores a simplified version of that challenge by asking:

- How does latency affect information spreading?
- How does packet loss reduce coordination?
- How does limited communication radius fragment the swarm?
- How do these constraints affect coverage and task completion?

---

## Core Features

### 1. Swarm agents
Each agent has:
- a position `(x, y)`
- a movement direction
- local communication ability
- simple rule-based behaviour

### 2. Communication model
Agents can only communicate when:
- they are within a fixed communication radius

The network also simulates:
- **latency**: messages arrive after a delay
- **packet loss**: some messages are dropped randomly

### 3. Task behaviour
Agents begin without target knowledge.

When an agent discovers the target:
- it becomes informed
- it shares that information with nearby agents
- other agents gradually become informed and move toward the target

This creates decentralised coordination.

### 4. Evaluation metrics
The project measures:
- **coverage**: how much of the environment has been explored
- **time to complete**: how long it takes before the target is discovered
- **coordination efficiency**: delivered messages divided by sent messages
- **signals received**: number of agents that successfully receive target information
- **messages sent, delivered, and dropped**

### 5. Experiments
The following scenarios are compared:
- baseline
- high latency
- high packet loss
- combined constraints

Each scenario is run multiple times using different random seeds.

### 6. Visualisation
The visual mode shows:
- agents moving in the environment
- communication links
- informed vs uninformed agents
- communication radius
- explored area heatmap
- live message statistics

---

## Project Structure

```text
Swarm-6G-Mini-Project/
│
├── agents.py
├── network.py
├── simulation.py
├── metrics.py
├── experiments.py
├── visualization.py
├── main.py
├── README.md
└── requirements.txt