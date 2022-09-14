# Andres Fonseca acz9et

from z3 import *

def hw2():

    X, Y, Z = Bools("X Y Z")
    
    # 1. X ∨ Y, X ⊢ ¬Y
    
    # As proposition in PL: ((X \/ Y) /\ X) -> Y
    C1 = Implies(And(Or(X, Y), X), Not(Y))
    
    s = Solver()
    s.add(Not(C1))
    
    s.check()
    isSat = s.check()
    
    #if Not(model) is unsat, then the model must be valid, if Not(model) is sat, model is not valid, but sat.
    if (isSat == unsat):
        print("model is valid")
    else:
        print("model is invalid")
        print(s.model())

hw2()