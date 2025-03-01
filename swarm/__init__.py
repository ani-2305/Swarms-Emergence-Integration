from dataclasses import dataclass
from typing import List, Callable, Dict, Any

@dataclass
class Result:
    """Result from an agent's execution."""
    success: bool
    output: str
    error: str = None

class Agent:
    """Base class for agents in the swarm system."""
    def __init__(self, name: str, description: str, functions: List[Callable], model: str = "gpt-4o"):
        self.name = name
        self.description = description
        self.functions = functions
        self.model = model

class Swarm:
    """Main class for managing swarm operations."""
    def __init__(self):
        self.agents = {}

    def run(self, agent: Agent, messages: List[Dict[str, str]], context_variables: Dict[str, Any] = None, max_turns: int = 5, debug: bool = False) -> Result:
        """Run an agent with the given messages and context."""
        try:
            # For now, just call the first function with the user's message
            if agent.functions and len(messages) > 0:
                user_message = messages[-1].get("content", "")
                response = agent.functions[0](user_message)
                return Result(success=True, output=response)
            return Result(success=False, error="No functions available or no messages provided")
        except Exception as e:
            return Result(success=False, error=str(e)) 