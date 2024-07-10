from __future__ import annotations
import propositions.Proposition

class Negation(propositions.Proposition.Proposition):
    def __init__(self, expression: str):
        super().__init__("¬(" + expression + ")")
