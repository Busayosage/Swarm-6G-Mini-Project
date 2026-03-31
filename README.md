# Swarm-6G Mini Project

A Python-based simulation exploring how communication constraints affect coordination in a simple multi-agent swarm.

This project is designed as a foundational step toward research in:

**Embodied Intelligence for 6G Enabled Robot Swarms**

---

## 🚀 Project Overview

This project simulates a group of agents moving in a 2D environment.

Agents:
- explore the environment
- discover a target
- communicate with nearby agents
- coordinate under communication constraints

The goal is to understand how **network limitations** impact swarm intelligence.

---

## 🧠 Key Features

### 1. Multi-Agent System
Each agent has:
- position (x, y)
- movement direction
- local communication ability
- simple rule-based behaviour

---

### 2. Communication Model

Agents communicate only within a fixed radius.

The network simulates:
- **Latency** → delayed message delivery  
- **Packet Loss** → messages randomly dropped  
- **Limited Range** → only nearby agents communicate  

---

### 3. Task Behaviour

Agents begin without knowledge of the target.

When an agent discovers the target:
- it becomes **informed**
- it shares information with neighbours
- other agents gradually become informed and move toward the target

This creates **decentralised coordination**

---

### 4. Evaluation Metrics

The system measures:

- **Coverage** → how much of the environment is explored  
- **Time to Completion** → how long it takes to reach the target  
- **Coordination Efficiency** → success of information spreading  
- **Signal Reach** → number of agents informed  
- **Communication Stats**:
  - messages sent
  - delivered
  - dropped  

---

### 5. Experiments

We compare multiple network conditions:

- Baseline (no constraints)
- High latency
- High packet loss
- Combined constraints

Each experiment runs multiple times using different random seeds.

---

## 📊 Visual Results

### 🔹 Exploration Stage

Agents initially explore the environment with no shared knowledge.

![Exploration](images/exploration.png)

---

### 🔹 Information Spread

Information about the target propagates through local communication links.

Edges represent communication between agents.

![Information Spread](images/information_spread.png)

---

### 🔹 Target Convergence

Informed agents coordinate and converge toward the target location.

![Target Convergence](images/target_convergence.png)

---

### 🔹 Coverage Heatmap

The heatmap shows how much of the environment has been explored over time.

![Coverage](images/coverage_heatmap.png)

---

## 📁 Project Structure

```
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
├── requirements.txt
│
├── images/
│   ├── exploration.png
│   ├── information_spread.png
│   ├── target_convergence.png
│   ├── coverage_heatmap.png
│
├── results/
```

---

## ⚙️ How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 2. Run the project

```bash
python main.py
```

---

### 3. Choose mode

- `1` → Run experiments  
- `2` → Run visual simulation  

---

## 🔬 Research Motivation

Future robot swarms operating in **6G-enabled environments** will depend on:

- reliable communication  
- low latency  
- efficient coordination  

This project explores how:

- latency affects information propagation  
- packet loss reduces coordination  
- communication range limits swarm efficiency  

---

## 🧩 Future Improvements

- Evolutionary optimisation of agent behaviour  
- Smarter coordination strategies  
- Reinforcement learning-based agents  
- Real-time performance dashboards  
- Advanced network models  

---

## 📌 Summary

This project demonstrates how simple agents can:

- coordinate using local communication  
- adapt to unreliable networks  
- exhibit swarm intelligence  

It provides a foundation for research in:

> **6G-enabled distributed robotic systems and embodied intelligence**

---
