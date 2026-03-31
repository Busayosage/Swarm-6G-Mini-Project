import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from agents import Agent
from network import Network


class VisualSwarmSimulation:
    def __init__(
        self,
        num_agents=15,
        width=100,
        height=100,
        communication_radius=20,
        latency_steps=0,
        packet_loss=0.0,
        target=(80, 80),
        target_radius=8,
        seed=None
    ):
        self.num_agents = num_agents
        self.width = width
        self.height = height
        self.target = target
        self.target_radius = target_radius

        if seed is not None:
            random.seed(seed)

        self.agents = self._create_agents()

        # ❌ No agent starts with target info

        self.network = Network(
            communication_radius=communication_radius,
            latency_steps=latency_steps,
            packet_loss=packet_loss
        )

        self.current_step = 0

        self.cell_size = 5
        self.visited_cells = set()

        self.fig, self.ax = plt.subplots(figsize=(7, 7))

    def _create_agents(self):
        agents = []
        for i in range(self.num_agents):
            x = random.uniform(0, self.width)
            y = random.uniform(0, self.height)
            agents.append(Agent(agent_id=i, x=x, y=y, speed=1.5))
        return agents

    def _send_messages(self):
        for sender in self.agents:
            message = sender.send_message()
            for receiver in self.agents:
                if sender.agent_id != receiver.agent_id:
                    self.network.try_send(sender, receiver, self.current_step, message)

    def update(self, frame):
        self.ax.clear()

        # 🔥 Movement logic
        for agent in self.agents:
            agent.random_turn()

            if agent.has_target_info:
                agent.move(self.width, self.height, target=self.target, target_pull=0.08)
            else:
                agent.move(self.width, self.height)

        # 🔥 Target discovery
        for agent in self.agents:
            distance = agent.distance_to_point(self.target)
            if distance <= self.target_radius:
                agent.has_target_info = True

        # 🔥 Coverage
        for agent in self.agents:
            cell_x = int(agent.x // self.cell_size)
            cell_y = int(agent.y // self.cell_size)
            self.visited_cells.add((cell_x, cell_y))

        self._send_messages()
        self.network.deliver_messages(self.agents, self.current_step)

        xs = [agent.x for agent in self.agents]
        ys = [agent.y for agent in self.agents]

        colors = []
        for agent in self.agents:
            if agent.has_target_info:
                colors.append("red")
            elif len(agent.received_messages) > 0:
                colors.append("yellow")
            else:
                colors.append("blue")

        # Coverage heatmap
        for (cell_x, cell_y) in self.visited_cells:
            self.ax.add_patch(
                plt.Rectangle(
                    (cell_x * self.cell_size, cell_y * self.cell_size),
                    self.cell_size,
                    self.cell_size,
                    color="lightblue",
                    alpha=0.2
                )
            )

        self.ax.scatter(xs, ys, c=colors, s=50, label="Agents")

        # Communication links
        for i, sender in enumerate(self.agents):
            for j, receiver in enumerate(self.agents):
                if i < j:
                    distance = sender.distance_to(receiver)
                    if distance <= self.network.communication_radius:
                        if random.random() < self.network.packet_loss:
                            self.ax.plot(
                                [sender.x, receiver.x],
                                [sender.y, receiver.y],
                                linewidth=0.5,
                                linestyle="dashed",
                                alpha=0.3
                            )
                        else:
                            self.ax.plot(
                                [sender.x, receiver.x],
                                [sender.y, receiver.y],
                                linewidth=1.0
                            )

        # Target
        self.ax.scatter(
            self.target[0],
            self.target[1],
            marker="*",
            s=250,
            label="Target"
        )

        # Radius
        first_agent = self.agents[0]
        circle = plt.Circle(
            (first_agent.x, first_agent.y),
            self.network.communication_radius,
            fill=False
        )
        self.ax.add_patch(circle)

        self.ax.set_xlim(0, self.width)
        self.ax.set_ylim(0, self.height)
        self.ax.set_title(f"Swarm Visualization - Step {self.current_step}")
        self.ax.legend(loc="upper right")

        # Metrics
        informed_count = sum(1 for agent in self.agents if agent.has_target_info)

        self.ax.text(0.02, 0.95, f"Step: {self.current_step}", transform=self.ax.transAxes)
        self.ax.text(0.02, 0.90, f"Informed Agents: {informed_count}/{len(self.agents)}", transform=self.ax.transAxes)
        self.ax.text(0.02, 0.85, f"Messages Sent: {self.network.total_sent}", transform=self.ax.transAxes)
        self.ax.text(0.02, 0.80, f"Delivered: {self.network.total_delivered}", transform=self.ax.transAxes)
        self.ax.text(0.02, 0.75, f"Dropped: {self.network.total_dropped}", transform=self.ax.transAxes)

        for agent in self.agents:
            agent.clear_messages()

        self.current_step += 1

    def run(self, steps=100):
        animation = FuncAnimation(
            self.fig,
            self.update,
            frames=steps,
            interval=200,
            repeat=False
        )
        plt.show()