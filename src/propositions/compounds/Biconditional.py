from __future__ import annotations
from propositions.compounds.Compound import Compound

class Biconditional(Compound):
    def operator(self) -> str:
        return "<->"
