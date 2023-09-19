from abc import ABC, abstractmethod
from typing import Dict
from .agent import Agent

class Game(ABC):
    def __init__(self, num_rounds: int = 1):
        """Initialize a Game instance."""
        self._agents: Dict[str, Agent] = {}
        self._num_rounds = max(1, num_rounds)

    def add_agent(self, agent: Agent):
        """Add an agent to the game."""
        self._agents[agent.name] = agent

    def remove_agent(self, name: str):
        """Remove an agent by its name."""
        if name in self._agents:
            del self._agents[name]

    def get_agent(self, name: str) -> Agent:
        """Get an agent by its name."""
        return self._agents.get(name, None)

    @abstractmethod
    def start_game(self):
        """Initialize the game."""
        pass

    @abstractmethod
    def play_round(self):
        """Conduct one round of the game."""
        pass

    @abstractmethod
    def evaluate_round(self):
        """Evaluate the round and update scores."""
        pass

    @abstractmethod
    def end_game(self):
        """Finalize the game and generate summary statistics."""
        pass

    def reset(self):
        """Reset the game state for a new run."""
        self._agents = {}
        self._num_rounds = 1
