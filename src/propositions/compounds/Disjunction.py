from __future__ import annotations
from propositions.compounds.Compound import Compound

class Disjunction(Compound):
    def operator(self) -> str:
        return "|"