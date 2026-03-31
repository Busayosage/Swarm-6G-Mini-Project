# Swarm-6G Mini Project

A simulation-based study of **multi-agent coordination under communication constraints**, designed as a foundational step toward research in:

> **Embodied Intelligence for 6G Enabled Robot Swarms**

---

## 🔬 Research Motivation

Future autonomous robot swarms operating in **6G-enabled environments** will rely on:

- ultra-low latency communication  
- reliable information exchange  
- distributed decision-making  

However, real-world networks are imperfect.

This project investigates:

- How does **latency** affect information propagation?  
- How does **packet loss** degrade coordination?  
- How does **limited communication range** fragment a swarm?  
- What is the impact on **coverage and task completion**?  

---

## 🧠 Methodology

We model a **decentralised multi-agent system** in a 2D environment.

Each agent:
- moves using simple stochastic motion  
- detects neighbours within a fixed radius  
- exchanges local messages  
- updates behaviour based on received information  

---

### 📡 Communication Model

The communication layer explicitly simulates:

- **Latency** → delayed message delivery  
- **Packet Loss** → probabilistic message dropping  
- **Communication Radius** → spatially constrained interaction  

This creates a realistic approximation of **imperfect wireless networks**

---

### 🎯 Task Definition

Agents must:

1. explore the environment  
2. discover a target  
3. propagate information  
4. coordinate movement toward the target  

This models **distributed sensing and coordination**

---

## 📊 Evaluation Metrics

We evaluate system performance using:

- **Coverage** → proportion of environment explored  
- **Time to Completion** → steps required to reach target  
- **Information Spread** → number of informed agents  
- **Communication Efficiency** →  
  - messages sent  
  - messages delivered  
  - messages dropped  

---

## 🧪 Experimental Design

We compare multiple network conditions:

- Baseline (ideal communication)  
- High latency  
- High packet loss  
- Combined constraints  

Each scenario is evaluated across multiple random seeds to ensure robustness.

---

## 📊 Visual Analysis

### 🔹 Exploration Phase

Agents initially explore independently without shared knowledge.

![Exploration](images/exploration.png)

---

### 🔹 Information Propagation

Information about the target spreads through local communication links.

Edges represent **agent-to-agent message exchange**.

![Information Spread](images/information_spread.png)

---

### 🔹 Coordinated Convergence

Informed agents collectively converge toward the target location.

This demonstrates emergent **swarm coordination**.

![Target Convergence](images/target_convergence.png)

---

### 🔹 Coverage Heatmap

The heatmap visualises spatial exploration over time.

![Coverage Heatmap](images/coverage_heatmap.png)

---

## 🧩 Key Insights

- Communication constraints significantly affect coordination speed  
- Packet loss reduces effective information propagation  
- Latency delays collective behaviour emergence  
- Local communication leads to **decentralised intelligence**  

---

## ⚙️ How to Run

```bash
pip install -r requirements.txt
python main.py
```

Choose:

- `1` → Run experiments  
- `2` → Run visual simulation  

---

## 📁 Project Structure

```
Swarm-6G-Mini-Project/
├── agents.py
├── network.py
├── simulation.py
├── metrics.py
├── experiments.py
├── visualization.py
├── main.py
├── README.md
├── requirements.txt
├── images/
├── results/
```

---

## 🚀 Future Work

- Reinforcement learning-based agent behaviour  
- Adaptive communication strategies  
- Dynamic network topology modelling  
- Integration with real robotic systems  
- Scaling to large swarm sizes  

---

## 📌 Conclusion

This project demonstrates how simple agents can achieve:

- decentralised coordination  
- adaptive behaviour under constraints  
- emergent swarm intelligence  

It provides a strong foundation for research in:

> **Distributed AI systems and 6G-enabled robotic swarms**