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

def hw2_9():
    X, Y, Z = Bools("X Y Z")
    
    # 9. X → Y, Y → X ⊢ X ↔ Y
    # As proposition in PL: ((X -> Y) /\ (Y -> X)) -> ((X -> Y) /\ (Y -> X))
    C1 = Implies(And(And(Implies(X, Y), Implies(Y, X))), And((Implies(X, Y), Implies(Y, X))))
    
    s = Solver()
    s.add(Not(C1))
    
    s.check()
    isSat = s.check()
    #if Not(model) is unsat, then the model must be valid, if Not(model) is sat, model is not valid, but sat.
    if (isSat == unsat):
        print("proposition 9 is valid")
    else:
        print("proposition 9 is not valid, counterexample:", s.model())

def hw2_10():
    X, Y, Z = Bools("X Y Z")
    
    # 10. X ↔ Y ⊢ X → Y
    # As proposition in PL: ((X -> Y) /\ (Y -> X)) -> (X -> Y)
    C1 = Implies(And(And(Implies(X, Y), Implies(Y,X))), Implies(X, Y))
    
    s = Solver()
    s.add(Not(C1))
    
    s.check()
    isSat = s.check()
    #if Not(model) is unsat, then the model must be valid, if Not(model) is sat, model is not valid, but sat.
    if (isSat == unsat):
        print("proposition 10 is valid")
    else:
        print("proposition 10 is not valid, counterexample:", s.model())

def hw2_11():
    X, Y, Z = Bools("X Y Z")
    
    # 11. X ↔ Y ⊢ Y → X
    # As proposition in PL: ((X -> Y) /\ (Y -> X)) -> (Y -> X)
    C1 = Implies(And(And(Implies(X, Y), Implies(Y,X))), Implies(Y, X))
    
    s = Solver()
    s.add(Not(C1))
    
    s.check()
    isSat = s.check()
    #if Not(model) is unsat, then the model must be valid, if Not(model) is sat, model is not valid, but sat.
    if (isSat == unsat):
        print("proposition 11 is valid")
    else:
        print("proposition 11 is not valid, counterexample:", s.model())

def hw2_12():
    X, Y, Z = Bools("X Y Z")
    
    # 12. X ∨ Y, X → Z, Y → Z ⊢ Z
    # As proposition in PL: ((X \/ Y) /\ (X -> Z)) /\ (Y -> Z) -> Z
    C1 = Implies(And(And(Or(X, Y), Implies(X, Z)), Implies(Y, Z)), Z)
    
    s = Solver()
    s.add(Not(C1))
    
    s.check()
    isSat = s.check()
    #if Not(model) is unsat, then the model must be valid, if Not(model) is sat, model is not valid, but sat.
    if (isSat == unsat):
        print("proposition 12 is valid")
    else:
        print("proposition 12 is not valid, counterexample:", s.model())

def hw2_13():
    X, Y, Z = Bools("X Y Z")
    
    # 13. X → Y, Y ⊢ X 
    # As proposition in PL: ((X -> Y) /\ (Y)) -> X
    C1 = Implies(And(Implies(X, Y), Y), X)
    
    s = Solver()
    s.add(Not(C1))
    
    s.check()
    isSat = s.check()
    #if Not(model) is unsat, then the model must be valid, if Not(model) is sat, model is not valid, but sat.
    if (isSat == unsat):
        print("proposition 13 is valid")
    else:
        print("proposition 13 is not valid, counterexample:", s.model())

def hw2_14():
    X, Y, Z = Bools("X Y Z")
    
    # 14. X → Y, X ⊢ Y
    # As proposition in PL: ((X -> Y) /\ X) -> Y
    C1 = Implies(And(Implies(X, Y), X), Y)
    
    s = Solver()
    s.add(Not(C1))
    
    s.check()
    isSat = s.check()
    #if Not(model) is unsat, then the model must be valid, if Not(model) is sat, model is not valid, but sat.
    if (isSat == unsat):
        print("proposition 14 is valid")
    else:
        print("proposition 14 is not valid, counterexample:", s.model())

def hw2_15():
    X, Y, Z = Bools("X Y Z")
    
    # 15. X → Y, Y → Z ⊢ X → Z
    # As proposition in PL: ((X -> Y) /\ (Y -> Z)) -> (X -> Z)
    C1 = Implies(And(Implies(X, Y), Implies(Y, Z)), Implies(X, Z))
    
    s = Solver()
    s.add(Not(C1))
    
    s.check()
    isSat = s.check()
    #if Not(model) is unsat, then the model must be valid, if Not(model) is sat, model is not valid, but sat.
    if (isSat == unsat):
        print("proposition 15 is valid")
    else:
        print("proposition 15 is not valid, counterexample:", s.model())

def hw2_16():
    X, Y, Z = Bools("X Y Z")
    
    # 16. X → Y ⊢ Y → X
    # As proposition in PL: ((X -> Y) -> (Y -> X)
    C1 = Implies(Implies(X, Y), Implies(Y, X))
    
    s = Solver()
    s.add(Not(C1))
    
    s.check()
    isSat = s.check()
    #if Not(model) is unsat, then the model must be valid, if Not(model) is sat, model is not valid, but sat.
    if (isSat == unsat):
        print("proposition 16 is valid")
    else:
        print("proposition 16 is not valid, counterexample:", s.model())

def hw2_17():
    X, Y, Z = Bools("X Y Z")
    
    # 17. X → Y ⊢ ¬Y → ¬X
    # As proposition in PL: ((X -> Y) -> (¬Y -> ¬X)
    C1 = Implies(Implies(X, Y), Implies(Not(Y), Not(X)))
    
    s = Solver()
    s.add(Not(C1))
    
    s.check()
    isSat = s.check()
    #if Not(model) is unsat, then the model must be valid, if Not(model) is sat, model is not valid, but sat.
    if (isSat == unsat):
        print("proposition 17 is valid")
    else:
        print("proposition 17 is not valid, counterexample:", s.model())

def hw2_18():
    X, Y, Z = Bools("X Y Z")
    
    # 18. ¬(X ∨ Y) ↔ ¬X ∧ ¬Y
    # As proposition in PL: (¬(X ∨ Y) -> (¬X ∧ ¬Y)) /\ ((¬X ∧ ¬Y) -> ¬(X ∨ Y))
    C1 = And(Implies(Not(Or(X, Y)), And(Not(X), Not(Y))), Implies(And(Not(X), Not(Y)), Not(Or(X, Y))))
    
    s = Solver()
    s.add(Not(C1))
    
    s.check()
    isSat = s.check()
    #if Not(model) is unsat, then the model must be valid, if Not(model) is sat, model is not valid, but sat.
    if (isSat == unsat):
        print("proposition 18 is valid")
    else:
        print("proposition 18 is not valid, counterexample:", s.model())

def hw2_19():
    X, Y, Z = Bools("X Y Z")
    
    # 19. ¬(X ∧ Y) ↔ ¬X ∨ ¬Y
    # As proposition in PL: (¬(X ∧ Y) -> (¬X ∨ ¬Y)) /\ ((¬X ∨ ¬Y) -> ¬(X ∧ Y))
    C1 = And(Implies(Not(And(X, Y)), Or(Not(X), Not(Y))), Implies(Or(Not(X), Not(Y)), Not(And(X, Y))))
    
    s = Solver()
    s.add(Not(C1))
    
    s.check()
    isSat = s.check()
    #if Not(model) is unsat, then the model must be valid, if Not(model) is sat, model is not valid, but sat.
    if (isSat == unsat):
        print("proposition 19 is valid")
    else:
        print("proposition 19 is not valid, counterexample:", s.model())

hw2_1()
hw2_2()
hw2_3()
hw2_4()
hw2_5()
hw2_6pt1()
hw2_6pt2()
hw2_7()
hw2_8()
hw2_9()
hw2_10()
hw2_11()
hw2_12()
hw2_13()
hw2_14()
hw2_15()
hw2_16()
hw2_17()
hw2_18()
hw2_19()