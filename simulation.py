import random

from agents import Agent
from network import Network
from metrics import MetricsTracker


class SwarmSimulation:
    def __init__(
        self,
        num_agents=15,
        width=100,
        height=100,
        steps=200,
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
        self.steps = steps
        self.target = target
        self.target_radius = target_radius

        if seed is not None:
            random.seed(seed)

        self.agents = self._create_agents()

        # First agent knows where the target is
        self.agents[0].has_target_info = True

        self.network = Network(
            communication_radius=communication_radius,
            latency_steps=latency_steps,
            packet_loss=packet_loss
        )

        self.metrics = MetricsTracker(width=width, height=height, cell_size=5)

    def _create_agents(self):
        agents = []
        for i in range(self.num_agents):
            x = random.uniform(0, self.width)
            y = random.uniform(0, self.height)
            agents.append(Agent(agent_id=i, x=x, y=y, speed=1.5))
        return agents

    def _send_messages(self, current_step):
        for sender in self.agents:
            message = sender.send_message()
            for receiver in self.agents:
                if sender.agent_id != receiver.agent_id:
                    self.network.try_send(sender, receiver, current_step, message)

    def _check_task_completion(self, step):
        for agent in self.agents:
            if agent.distance_to_point(self.target) <= self.target_radius:
                self.metrics.mark_task_complete(step)
                break

    def step(self, current_step):
        for agent in self.agents:
            agent.random_turn()
            agent.move(self.width, self.height, target=self.target, target_pull=0.08)

        self._send_messages(current_step)
        self.network.deliver_messages(self.agents, current_step)

        self.metrics.update_coverage(self.agents)
        self._check_task_completion(current_step)

        for agent in self.agents:
            agent.clear_messages()

    def run(self):
        for step in range(self.steps):
            self.step(step)

            if self.metrics.task_completed:
                break

        results = self.metrics.get_results(self.network, self.agents)

        if results["time_to_complete"] is None:
            results["time_to_complete"] = self.steps

        return results