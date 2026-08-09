# grid_game.py
import random


class GridHuntGame:
    """A small Pacman-style grid environment (4x4) where an agent collects food."""

    #This creates a 4 × 4 grid.
    def __init__(self, width=4, height=4):
        self.width = width
        self.height = height
        self.agent_pos = [0, 0]  # Starting position (x, y)

        # Place a few random food pellets and obstacles (walls)
        self.food_positions = {(1, 2), (2, 3), (3, 0), (2, 1)}
        # There are two walls.
        self.walls = {(1, 1), (2, 2)}

        #Initial score and steps
        self.score = 0
        self.steps = 0

    #tell agent, what can currently perceive
    def get_percept(self, agent) -> dict:
        return {
            #Tells the agent its current position
            'agent_pos': list(self.agent_pos),
            #Is there food at my current position?
            'smells_food': tuple(self.agent_pos) in self.food_positions,
            #Tells whether the current position is a wall
            'hit_wall': tuple(self.agent_pos) in self.walls,
            #The agent can see its current score
            'score': self.score,
            #Tells the agent how many food pellets remain
            'remaining_food': len(self.food_positions)
        }

    #environment receives an action from the agent
    def execute_action(self, agent, action: str):
        self.steps += 1
        new_pos = list(self.agent_pos)
        #The environment moves the agent
        if action == 'Up':
            new_pos[1] = min(self.height - 1, new_pos[1] + 1)
        elif action == 'Down':
            new_pos[1] = max(0, new_pos[1] - 1)
        elif action == 'Left':
            new_pos[0] = max(0, new_pos[0] - 1)
        elif action == 'Right':
            new_pos[0] = min(self.width - 1, new_pos[0] + 1)

        # Check collision with walls
        if tuple(new_pos) in self.walls:
            self.score -= 5  # Penalty for hitting a wall
        else:
            self.agent_pos = new_pos

        # Check if eating food
        tuple_pos = tuple(self.agent_pos)
        if tuple_pos in self.food_positions:
            self.food_positions.remove(tuple_pos)
            self.score += 20  # Reward for eating food pellet

    #The game ends when
    #No food remains OR 20 steps have been reached
    def is_done(self) -> bool:
        return len(self.food_positions) == 0 or self.steps >= 20