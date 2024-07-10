from __future__ import annotations
from propositions.Proposition import Proposition
from abc import ABC, abstractmethod

class Compound(Proposition, ABC):
    left: Proposition
    right: Proposition

    def __init__(self, left: Proposition, right: Proposition):
        super().__init__(
            left.expression + f' {self.operator()} ' + right.expression)
        self.left = left
        self.right = right
    
    @abstractmethod
    def operator(self) -> str:
        ...
