from __future__ import annotations
from typing import Any

class Proposition:
    expression: str
    
    def __init__(self, expression: str):
        self.expression = expression
    
    def negated(self):
        from propositions.Negation import Negation
        return Negation(self.expression)

    def __eq__(self, other: Any):
        return (self.expression == other.expression)

    def __hash__(self) -> int:
        return hash(self.expression)

    def __repr__(self) -> str:
        return self.expression