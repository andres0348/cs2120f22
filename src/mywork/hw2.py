# Andres Fonseca acz9et

from z3 import *

def hw2_1():
    X, Y, Z = Bools("X Y Z")
    
    # 1. X ∨ Y, X ⊢ ¬Y
    # As proposition in PL: ((X \/ Y) /\ X) -> ¬Y
    C1 = Implies(And(Or(X, Y), X), Not(Y))
    
    s = Solver()
    s.add(Not(C1))
    
    s.check()
    isSat = s.check()
    
    #if Not(model) is unsat, then the model must be valid, if Not(model) is sat, model is not valid, but sat.
    if (isSat == unsat):
        print("proposition 1 is valid")
    else:
        print("proposition 1 is not valid, counterexample:", s.model())

def hw2_2():
    X, Y, Z = Bools("X Y Z")
    
    # 2. X, Y ⊢ X ∧ Y
    # As proposition in PL: ((X /\ Y) -> X /\ Y )
    C1 = Implies(And(X, Y), And(X, Y))
    
    s = Solver()
    s.add(Not(C1))
    
    s.check()
    isSat = s.check()
    
    #if Not(model) is unsat, then the model must be valid, if Not(model) is sat, model is not valid, but sat.
    if (isSat == unsat):
        print("proposition 2 is valid")
    else:
        print("proposition 2 is not valid, counterexample:", s.model())

def hw2_3():
    X, Y, Z = Bools("X Y Z")
    
    # 3. X ∧ Y ⊢ X
    # As proposition in PL: ((X /\ Y) -> X)
    C1 = Implies(And(X, Y), X)
    
    s = Solver()
    s.add(Not(C1))
    
    s.check()
    isSat = s.check()
    
    #if Not(model) is unsat, then the model must be valid, if Not(model) is sat, model is not valid, but sat.
    if (isSat == unsat):
        print("proposition 3 is valid")
    else:
        print("proposition 3 is not valid, counterexample:", s.model())

def hw2_4():
    X, Y, Z = Bools("X Y Z")
    
    # 4. X ∧ Y ⊢ Y
    # As proposition in PL: ((X /\ Y) -> X)
    C1 = Implies(And(X, Y), Y)
    
    s = Solver()
    s.add(Not(C1))
    
    s.check()
    isSat = s.check()
    
    #if Not(model) is unsat, then the model must be valid, if Not(model) is sat, model is not valid, but sat.
    if (isSat == unsat):
        print("proposition 4 is valid")
    else:
        print("proposition 4 is not valid, counterexample:", s.model())

def hw2_5():
    X, Y, Z = Bools("X Y Z")
    
    # 5. ¬¬X ⊢ X
    # As proposition in PL: ¬¬X -> X
    C1 = Implies(Not(Not(X)), X)
    
    s = Solver()
    s.add(Not(C1))
    
    s.check()
    isSat = s.check()
    #if Not(model) is unsat, then the model must be valid, if Not(model) is sat, model is not valid, but sat.
    if (isSat == unsat):
        print("proposition 5 is valid")
    else:
        print("proposition 5 is not valid, counterexample:", s.model())

def hw2_6pt1():
    X, Y, Z = Bools("X Y Z")
    
    # 6. ¬(X ∧ ¬X)
    # As proposition in PL: ¬¬X -> X
    C1 = Not(And(X, Not(X)))
    
    s = Solver()
    s.add(Not(C1))
    
    s.check()
    isSat = s.check()
    #if Not(model) is unsat, then the model must be valid, if Not(model) is sat, model is not valid, but sat.
    if (isSat == unsat):
        print("proposition 6.1 is valid")
    else:
        print("proposition 6.1 is not valid, counterexample:", s.model())

def hw2_6pt2():
    X, Y, Z = Bools("X Y Z")
    
    # 6. X ⊢ X ∨ Y
    # As proposition in PL: X -> (X \/ Y)
    C1 = Implies(X, Or(X, Y))
    
    s = Solver()
    s.add(Not(C1))
    
    s.check()
    isSat = s.check()
    #if Not(model) is unsat, then the model must be valid, if Not(model) is sat, model is not valid, but sat.
    if (isSat == unsat):
        print("proposition 6.2 is valid")
    else:
        print("proposition 6.2 is not valid, counterexample:", s.model())

def hw2_7():
    X, Y, Z = Bools("X Y Z")
    
    # 7. Y ⊢ X ∨ Y
    # As proposition in PL: Y -> (X \/ Y)
    C1 = Implies(Y, Or(X, Y))
    
    s = Solver()
    s.add(Not(C1))
    
    s.check()
    isSat = s.check()
    #if Not(model) is unsat, then the model must be valid, if Not(model) is sat, model is not valid, but sat.
    if (isSat == unsat):
        print("proposition 7 is valid")
    else:
        print("proposition 7 is not valid, counterexample:", s.model())

def hw2_8():
    X, Y, Z = Bools("X Y Z")
    
    # 8. X → Y, ¬X ⊢ ¬Y
    # As proposition in PL: (X -> Y) /\ ¬X -> ¬Y
    C1 = Implies(And(Implies(X, Y), Not(X)) , Not(Y))
    
    s = Solver()
    s.add(Not(C1))
    
    s.check()
    isSat = s.check()
    #if Not(model) is unsat, then the model must be valid, if Not(model) is sat, model is not valid, but sat.
    if (isSat == unsat):
        print("proposition 8 is valid")
    else:
        print("proposition 8 is not valid, counterexample:", s.model())



hw2_1()
hw2_2()
hw2_3()
hw2_4()
hw2_5()
hw2_6pt1()
hw2_6pt2()
hw2_7()
hw2_8()

