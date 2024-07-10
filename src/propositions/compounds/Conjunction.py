from __future__ import annotations
from propositions.compounds.Compound import Compound

class Conjunction(Compound):
    def operator(self) -> str:
        return "&"
