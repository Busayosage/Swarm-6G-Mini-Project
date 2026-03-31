import math
import random


class Agent:
    def __init__(self, agent_id, x, y, speed=1.0):
        self.agent_id = agent_id
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = random.uniform(0, 2 * math.pi)
        self.received_messages = []
        self.has_target_info = False

    def move(self, width, height, target=None, target_pull=0.05):
        """
        Move the agent.
        If the agent has target info, it is slightly pulled toward the target.
        Otherwise it mostly moves randomly.
        """
        if self.has_target_info and target is not None:
            dx = target[0] - self.x
            dy = target[1] - self.y
            angle_to_target = math.atan2(dy, dx)
            self.direction = (1 - target_pull) * self.direction + target_pull * angle_to_target

        self.x += self.speed * math.cos(self.direction)
        self.y += self.speed * math.sin(self.direction)

        # Bounce off boundaries
        if self.x < 0:
            self.x = 0
            self.direction = math.pi - self.direction
        elif self.x > width:
            self.x = width
            self.direction = math.pi - self.direction

        if self.y < 0:
            self.y = 0
            self.direction = -self.direction
        elif self.y > height:
            self.y = height
            self.direction = -self.direction

    def random_turn(self, turn_angle=0.3):
        self.direction += random.uniform(-turn_angle, turn_angle)

    def distance_to(self, other_agent):
        return math.sqrt((self.x - other_agent.x) ** 2 + (self.y - other_agent.y) ** 2)

    def distance_to_point(self, point):
        return math.sqrt((self.x - point[0]) ** 2 + (self.y - point[1]) ** 2)

    def send_message(self):
        return {
            "sender_id": self.agent_id,
            "x": self.x,
            "y": self.y,
            "has_target_info": self.has_target_info
        }

    def receive_message(self, message):
        self.received_messages.append(message)

        if message.get("has_target_info", False):
            self.has_target_info = True

    def clear_messages(self):
        self.received_messages = []