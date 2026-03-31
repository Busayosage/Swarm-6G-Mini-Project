class MetricsTracker:
    def __init__(self, width, height, cell_size=5):
        self.width = width
        self.height = height
        self.cell_size = cell_size

        self.visited_cells = set()
        self.steps_taken = 0
        self.task_completed = False
        self.task_completion_step = None

    def update_coverage(self, agents):
        for agent in agents:
            cell_x = int(agent.x // self.cell_size)
            cell_y = int(agent.y // self.cell_size)
            self.visited_cells.add((cell_x, cell_y))

    def coverage_ratio(self):
        total_cells_x = int(self.width // self.cell_size) + 1
        total_cells_y = int(self.height // self.cell_size) + 1
        total_cells = total_cells_x * total_cells_y

        if total_cells == 0:
            return 0.0

        return len(self.visited_cells) / total_cells

    def mark_task_complete(self, step):
        if not self.task_completed:
            self.task_completed = True
            self.task_completion_step = step

    def get_results(self, network, agents):
        informed_agents = sum(1 for agent in agents if agent.has_target_info)

        coordination_efficiency = 0.0
        if network.total_sent > 0:
            coordination_efficiency = network.total_delivered / network.total_sent

        return {
            "coverage": self.coverage_ratio(),
            "task_completed": self.task_completed,
            "time_to_complete": self.task_completion_step if self.task_completed else None,
            "coordination_efficiency": coordination_efficiency,
            "signals_received_agents": informed_agents,
            "messages_sent": network.total_sent,
            "messages_delivered": network.total_delivered,
            "messages_dropped": network.total_dropped
        }