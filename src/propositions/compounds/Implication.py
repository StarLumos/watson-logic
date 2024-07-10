from __future__ import annotations
from propositions.compounds.Compound import Compound
from propositions.Proposition import Proposition

class Implication(Compound): 
    def operator(self) -> str:
        return "->"
    
    @property
    def antecedent(self) -> Proposition:
        return self.left
    @antecedent.setter
    def antecedent(self, value: Proposition) -> None:
        self.left = value
    
    @property
    def consequent(self) -> Proposition:
        return self.right
    @consequent.setter
    def consequent(self, value: Proposition) -> None:
         self.right = value
