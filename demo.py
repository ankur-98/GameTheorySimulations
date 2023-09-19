from typing import Tuple, List, Callable, Dict

class Agent:
    def __init__(self, name: str):
        self.name = name
        self.choice = None
    
    def make_choice(self, strategy: Callable):
        self.choice = strategy()
        
class Strategy:
    @staticmethod
    def random_strategy():
        import random
        return 'C' if random.random() > 0.5 else 'B'

    @staticmethod
    def always_cooperate():
        return 'C'

    @staticmethod
    def always_betray():
        return 'B'

class PrisonersDilemma:
    def __init__(self, agent1: Agent, agent2: Agent, payoff_matrix: Dict[Tuple[str, str], Tuple[int, int]]):
        self.agent1 = agent1
        self.agent2 = agent2
        self.payoff_matrix = payoff_matrix

    def play_round(self, strategy1: Callable, strategy2: Callable) -> Tuple[int, int]:
        self.agent1.make_choice(strategy1)
        self.agent2.make_choice(strategy2)
        payoff = self.payoff_matrix[(self.agent1.choice, self.agent2.choice)]
        return payoff

    def simulate_game(self, rounds: int, strategy1: Callable, strategy2: Callable) -> List[Tuple[int, int]]:
        results = []
        for _ in range(rounds):
            payoff = self.play_round(strategy1, strategy2)
            print(f"Round Payoffs: {self.agent1.name} = {payoff[0]}, {self.agent2.name} = {payoff[1]}")
            results.append(payoff)
        return results

if __name__ == "__main__":
    # Define Payoff Matrix: (C=Cooperate, B=Betray)
    payoff_matrix = {
        ('C', 'C'): (3, 3),
        ('C', 'B'): (0, 5),
        ('B', 'C'): (5, 0),
        ('B', 'B'): (1, 1),
    }

    # Create Agents
    alice = Agent("Alice")
    bob = Agent("Bob")

    # Initialize Game
    game = PrisonersDilemma(alice, bob, payoff_matrix)

    # Simulate the game for 5 rounds using random strategies
    print("\nSimulating the gameplay for 5 rounds using random strategies..")
    game.simulate_game(5, Strategy.random_strategy, Strategy.random_strategy)

    # Simulate the game for 5 rounds using always cooperate strategies
    print("\nSimulating the gameplay for 5 rounds using always cooperate strategies..")
    game.simulate_game(1, Strategy.always_cooperate, Strategy.always_cooperate)

    # Simulate the game for 5 rounds using always betray strategies
    print("\nSimulating the gameplay for 5 rounds using always betray strategies..")
    game.simulate_game(1, Strategy.always_betray, Strategy.always_betray)
    