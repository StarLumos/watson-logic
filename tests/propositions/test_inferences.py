from src.propositions.Proposition import Proposition
from src.inferences import HypotheticalSyllogism, ModusPonens, ModusTollens
from src.propositions.compounds.Implication import Implication

def test_negation():
    assert Proposition("It is Saturday").negated().expression == "¬(It is Saturday)"

def test_modus_ponens():
    p = Proposition("p")
    q = Proposition("q")

    assert ModusPonens(
        Implication(p, q),
        p
    ) == q

def test_modus_tollens():
    p = Proposition("p")
    q = Proposition("q")

    assert ModusTollens(
        Implication(p, q),
        q.negated()
    ) == p.negated()

def test_hypothetical_syllogism():
    a = Proposition("It is hot")
    b = Proposition("I need to turn on the AC")
    c = Proposition("I need to pay my electricity bill")

    assert HypotheticalSyllogism(
        Implication(a, b),
        Implication(b, c)
    ) == Implication(a, c)
