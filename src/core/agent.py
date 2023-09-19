from abc import ABC, abstractmethod
from typing import Optional

class Agent(ABC):
    def __init__(self, name: str, initial_strategy: Optional[str] = None, initial_score: int = 0):
        self.name = name
        self.strategy = initial_strategy
        self.score = initial_score

    @abstractmethod
    def make_decision(self):
        """Make a decision based on the current strategy."""
        pass

    @abstractmethod
    def receive_communication(self, message):
        """Process incoming message or signal."""
        pass

    @abstractmethod
    def send_communication(self):
        """Send message or signal based on the current state or strategy."""
        pass

    @abstractmethod
    def update_strategy(self, new_strategy):
        """Dynamically update the agent's strategy."""
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, strategy={self.strategy}, score={self.score})"
