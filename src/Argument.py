from typing import Any
import inspect
from propositions.Proposition import Proposition
from inferences import ModusPonens, ModusTollens, HypotheticalSyllogism, Absorption, ConjunctionIntroduction, ConjunctionElimination, DisjunctionIntroduction, DisjunctionElimination, DisjunctiveSyllogism, DisjunctiveSimplification, Resolution, BiconditionalIntroduction

def parameter_types(fn: Any) -> list[Any]:
    sig = inspect.signature(fn)
    params = list(sig.parameters.values())
    param_types = [param.annotation for param in params]
    return param_types

class Argument:
    premises: set[Proposition]
    conclusion: Proposition
    
    def __init__(self, premises: set[Proposition], conclusion: Proposition):
        self.premises = premises
        self.conclusion = conclusion

def valid(argument: Argument) -> bool:
    def recurse(entailment: Proposition):
        argument.premises.add(entailment)
        return valid(argument)

    unary = { Absorption, ConjunctionElimination, DisjunctiveSimplification }
    for premise in argument.premises:
        for rule in unary:
            if isinstance(premise, eval(parameter_types(rule)[0])):
                entailment = rule(premise) # type: ignore
                if entailment:
                    if entailment == argument.conclusion:
                        return True
                    else:
                        return recurse(entailment)

    binary = { ModusPonens, ModusTollens, HypotheticalSyllogism, ConjunctionIntroduction, DisjunctionIntroduction, DisjunctiveSyllogism, Resolution, BiconditionalIntroduction }
    for p1 in argument.premises:
        for p2 in argument.premises:
            for rule in binary:
                parameters = parameter_types(rule)
                if isinstance(p1, eval(parameters[0])) and isinstance(p2, eval(parameters[1])):
                    entailment = rule(p1, p2) # type: ignore
                    if entailment:
                        if entailment == argument.conclusion:
                            return True
                        else:
                            return recurse(entailment)

    trinary = { DisjunctionElimination }
    for p1 in argument.premises:
        for p2 in argument.premises:
            for p3 in argument.premises:
                for rule in trinary:
                    try:
                        entailment = rule(p1, p2, p3) # type: ignore
                        if entailment:
                            if entailment == argument.conclusion:
                                return True
                            else:
                                return recurse(entailment)
                    except:
                        continue

    return False
