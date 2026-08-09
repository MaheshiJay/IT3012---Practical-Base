# agent.py
import random

#current starter agent
class GreedyGridAgent:
    """A simple agent that tries to move around systematically to clear the grid."""

    def __init__(self):
        self.actions_pool = ['Up', 'Down', 'Left', 'Right']

    def sense_and_act(self, percept: dict) -> str:
        # If standing directly on food, or just wander / move towards coordinates
        pos = percept['agent_pos']

        # agent doesn't actually make an intelligent decision
        #It randomly chooses up,down,left, right
        return random.choice(self.actions_pool)