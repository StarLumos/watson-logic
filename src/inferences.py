from __future__ import annotations
from propositions.compounds.Conjunction import Conjunction
from propositions.compounds.Disjunction import Disjunction
from propositions.compounds.Implication import Implication
from propositions.Proposition import Proposition
from propositions.Negation import Negation
from propositions.compounds.Biconditional import Biconditional

def ModusPonens(p1: Implication, p2: Proposition) -> Proposition | None:
    if p2 == p1.antecedent:
        return p1.consequent

def ModusTollens(p1: Implication, p2: Proposition) -> Negation | None:
    if p2 == p1.consequent.negated():
        return p1.antecedent.negated()

def HypotheticalSyllogism(p1: Implication, p2: Implication) -> Implication | None:
    if p1.consequent == p2.antecedent:
        return Implication(p1.antecedent, p2.consequent)

def Absorption(p1: Implication) -> Implication | None:
    return Implication(p1.antecedent, Conjunction(p1.antecedent, p1.consequent))

def ConjunctionIntroduction(p1: Proposition, p2: Proposition) -> Conjunction | None:
    return Conjunction(p1, p2)

def ConjunctionElimination(p1: Conjunction) -> Proposition | None:
    return p1.left and p1.right

def DisjunctionIntroduction(p1: Proposition, p2: Proposition) -> Disjunction | None:
    return Disjunction(p1, p2)

def DisjunctionElimination(p1: Implication, p2: Implication, p3: Disjunction) -> Proposition | None:
    if p1.consequent == p2.consequent:
        if p1.antecedent == p3.left and p2.antecedent == p3.right:
            return p1.consequent

def DisjunctiveSyllogism(p1: Disjunction, p2: Negation) -> Proposition | None:
    if p2 == p1.left.negated():
        return p1.right
    if p2 == p1.right.negated():
        return p1.left

def DisjunctiveSimplification(p1: Disjunction) -> Proposition | None:
    if p1.left == p1.right:
        return p1.left

def Resolution(p1: Disjunction, p2: Disjunction) -> Disjunction | None:
    if p1.left.negated() == p2.left:
        return Disjunction(p1.right, p2.right)

def BiconditionalIntroduction(p1: Implication, p2: Implication) -> Biconditional | None:
    if p1.left == p2.right and p1.right == p2.left:
        return Biconditional(p1.left, p1.right)

# def DoubleNegation(p1: Negation) -> Proposition | None:
#     if "¬(¬(" in p1.expression:
        
