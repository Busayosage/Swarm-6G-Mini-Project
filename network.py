import random


class Network:
    def __init__(self, communication_radius=15, latency_steps=0, packet_loss=0.0):
        self.communication_radius = communication_radius
        self.latency_steps = latency_steps
        self.packet_loss = packet_loss

        # Messages waiting for delivery
        self.message_queue = []

        # Counters for metrics
        self.total_sent = 0
        self.total_dropped = 0
        self.total_delivered = 0
        self.unique_receivers = set()

    def try_send(self, sender, receiver, current_step, message):
        """
        Send a message if:
        - receiver is within communication radius
        - message is not dropped by packet loss
        """
        distance = sender.distance_to(receiver)

        if distance > self.communication_radius:
            return

        self.total_sent += 1

        # Packet loss check
        if random.random() < self.packet_loss:
            self.total_dropped += 1
            return

        delivery_step = current_step + self.latency_steps

        self.message_queue.append({
            "delivery_step": delivery_step,
            "receiver_id": receiver.agent_id,
            "message": message
        })

    def deliver_messages(self, agents, current_step):
        """
        Deliver messages that have reached their delivery time.
        """
        remaining_queue = []

        agent_dict = {agent.agent_id: agent for agent in agents}

        for item in self.message_queue:
            if item["delivery_step"] <= current_step:
                receiver_id = item["receiver_id"]
                if receiver_id in agent_dict:
                    agent_dict[receiver_id].receive_message(item["message"])
                    self.total_delivered += 1
                    self.unique_receivers.add(receiver_id)
            else:
                remaining_queue.append(item)

        self.message_queue = remaining_queue