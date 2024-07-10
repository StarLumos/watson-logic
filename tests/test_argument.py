from Argument import Argument, valid
from inferences import HypotheticalSyllogism, ModusPonens, ModusTollens
from propositions.compounds.Implication import Implication
from propositions.Proposition import Proposition
from propositions.compounds.Conjunction import Conjunction
from propositions.compounds.Disjunction import Disjunction

def test_negation():
    assert Proposition("It is Saturday").negated().expression == "¬(It is Saturday)"

def test_Absorption():
    assert valid(Argument(
        premises = {
            Implication(Proposition('p'), Proposition('q')),
        },
        conclusion = Implication(
            Proposition('p'), 
            Conjunction(
                Proposition('p'), Proposition('q')
            ))
        ))

def test_ConjunctionElimination():
    assert valid(Argument(
        premises = {
            Conjunction(Proposition('p'), Proposition('q'))
        },
        conclusion = Proposition('p') and Proposition('q')
    ))

def test_DisjunctiveSimplification():
    assert valid(Argument(
        premises = {
            Disjunction(Proposition('p'), Proposition('p')),
        },
        conclusion = Proposition('p')
    ))

# we can test if the inference rules themselves are properly defined
# or we can test our argument validator logic for scanning
# an argument that USES inference rules.

# the line between the two in how useful they are gets blurred the smaller the test is.

def test_ModusPonensChains():
    assert valid(Argument(
        premises = { 
            Implication(Proposition('p'), Proposition('q')),
            Implication(Proposition('q'), Proposition('r')),
            # Implication(Proposition('r'), Proposition('s')),
            # Implication(Proposition('s'), Proposition('k')),
            Proposition('p')
        },
        conclusion = Proposition('r')
    ))

# def test_ModusPonens():
#     # convert this to an Argument that utilizes the ModusPonens rule logic
    
    
#     p = Proposition("p")
#     q = Proposition("q")

#     assert ModusPonens(
#         Implication(Proposition("p"), q),
#         p
#     ) == q

# def test_modus_tollens():
#     p = Proposition("p")
#     q = Proposition("q")

#     assert ModusTollens(
#         Implication(p, q),
#         q.negated()
#     ) == p.negated()

# def test_hypothetical_syllogism():
#     a = Proposition("It is hot")
#     b = Proposition("I need to turn on the AC")
#     c = Proposition("I need to pay my electricity bill")

#     assert HypotheticalSyllogism(
#         Implication(a, b),
#         Implication(b, c)
#     ) == Implication(a, c)