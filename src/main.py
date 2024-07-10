from __future__ import annotations
from Argument import valid, Argument
from propositions.Proposition import Proposition
from propositions.compounds.Implication import Implication

argument = Argument(
        premises = { 
            Implication(Proposition('p'), Proposition('q')),
            Implication(Proposition('q'), Proposition('r')),
            Proposition('p')
        },
        conclusion = Proposition('r')
    )

valid(argument)

# TODO: find a way to solve infinite recursive problem (where one rule is being applied to the same proposition due to the propositions being saved in the set even when they're already "solved") (ie: applying absorption over and over again to the same implication)
