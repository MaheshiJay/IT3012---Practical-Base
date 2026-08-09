# simulator.py
from grid_game import GridHuntGame
from agent import GreedyGridAgent

def run_grid_hunt():
    #Create Environment
    env = GridHuntGame()
    #Create Agent
    agent = GreedyGridAgent()

    print("=== UC Berkeley Style Small Grid Hunt Started ===")

    #Keep running until the environment says Game over
    while not env.is_done():
        #The environment gives information to the agent.
        percept = env.get_percept(agent)   #-->SENSOR

        #The agent receives the percept and decides what to do.
        action = agent.sense_and_act(percept)  # AGENT DECISION

        #The environment executes the agent's action.
        env.execute_action(agent, action)   # ACTUATOR / ACTION
        print(f"Pos: {percept['agent_pos']} | Food Left: {percept['remaining_food']} | Score: {percept['score']}")

    print(f"\nGame Over! Final Score: {env.score} after {env.steps} steps.")

if __name__ == "__main__":
    run_grid_hunt()