# Andres Fonseca acz9et

from z3 import *
X, Y, Z = Bools("X Y Z")

props = []

# 1. X ∨ Y, X ⊢ ¬Y
# As proposition in PL: ((X \/ Y) /\ X) -> ¬Y   
C1 = Implies(And(Or(X, Y), X), Not(Y))
# If x = is raining and y = slippery roads, if it is raining or the roads are slippery, and it is given
# that it's raining, hen slippery roads must be false to fulfill this inference rule. Since there
# could be rain and slippery roads(both true), this inference rule is not valid.
props.append(C1)

# 2. X, Y ⊢ X ∧ Y
# As proposition in PL: ((X /\ Y) -> X /\ Y )
C2 = Implies(And(X, Y), And(X, Y))
props.append(C2)

# 3. X ∧ Y ⊢ X
# As proposition in PL: ((X /\ Y) -> X)
C3 = Implies(And(X, Y), X)
props.append(C3)

# 4. X ∧ Y ⊢ Y
# As proposition in PL: ((X /\ Y) -> X)
C4 = Implies(And(X, Y), Y)
props.append(C4)

# 5. ¬¬X ⊢ X
# As proposition in PL: ¬¬X -> X
C5 = Implies(Not(Not(X)), X)
props.append(C5)

# 6. ¬(X ∧ ¬X)
# As proposition in PL: ¬¬X -> X
C6_0 = Not(And(X, Not(X)))
props.append(C6_0)

# 6. X ⊢ X ∨ Y
# As proposition in PL: X -> (X \/ Y)
C6_1 = Implies(X, Or(X, Y))
props.append(C6_1)

# 7. Y ⊢ X ∨ Y
# As proposition in PL: Y -> (X \/ Y)
C7 = Implies(Y, Or(X, Y))
props.append(C7)

# 8. X → Y, ¬X ⊢ ¬Y
# As proposition in PL: (X -> Y) /\ ¬X -> ¬Y
C8 = Implies(And(Implies(X, Y), Not(X)) , Not(Y))
# If x = is raining and y = slippery roads; if rain implies slippery roads (x->y), and it is not  
# raining (¬x), then the roads can't be slippery(¬y). However, if it is not raining and roads are slippery 
# from an oil spill(for example), then this proposition would not hold up, since the proposition 
# simplifies to true -> false, which is false (when x:false, y:true)
props.append(C8)

# 9. X → Y, Y → X ⊢ X ↔ Y
# As proposition in PL: ((X -> Y) /\ (Y -> X)) -> ((X -> Y) /\ (Y -> X))
C9 = Implies(And(And(Implies(X, Y), Implies(Y, X))), And((Implies(X, Y), Implies(Y, X))))
props.append(C9)

# 10. X ↔ Y ⊢ X → Y
# As proposition in PL: ((X -> Y) /\ (Y -> X)) -> (X -> Y)
C10 = Implies(And(And(Implies(X, Y), Implies(Y,X))), Implies(X, Y))
props.append(C10)

# 11. X ↔ Y ⊢ Y → X
# As proposition in PL: ((X -> Y) /\ (Y -> X)) -> (Y -> X)
C11 = Implies(And(And(Implies(X, Y), Implies(Y,X))), Implies(Y, X))
props.append(C11)

# 12. X ∨ Y, X → Z, Y → Z ⊢ Z
# As proposition in PL: ((X \/ Y) /\ (X -> Z)) /\ (Y -> Z) -> Z
C12 = Implies(And(And(Or(X, Y), Implies(X, Z)), Implies(Y, Z)), Z)
props.append(C12)

# 13. X → Y, Y ⊢ X 
# As proposition in PL: ((X -> Y) /\ (Y)) -> X
C13 = Implies(And(Implies(X, Y), Y), X)
# If x = israining and y = slippery roads, if roads are slippery when raining (x->y) and the roads are 
# slippery (y:true), then it must be raining (...->x). However, if it is not raining and the roads are
# slippery for other reasons (x:false, y:true), then the left-side conditions still hold up, even 
# though it isn't raining
props.append(C13)

# 14. X → Y, X ⊢ Y
# As proposition in PL: ((X -> Y) /\ X) -> Y
C14 = Implies(And(Implies(X, Y), X), Y)
props.append(C14)

# 15. X → Y, Y → Z ⊢ X → Z
# As proposition in PL: ((X -> Y) /\ (Y -> Z)) -> (X -> Z)
C15 = Implies(And(Implies(X, Y), Implies(Y, Z)), Implies(X, Z))
props.append(C15)

# 16. X → Y ⊢ Y → X
# As proposition in PL: ((X -> Y) -> (Y -> X)
C16 = Implies(Implies(X, Y), Implies(Y, X))
# if x = israining and y = slippery roads, if rain implies slippery roads (x->y) then slippery roads
# must imply rain (y->x). However, this condition does not hold up when it is not raining and roads
# are slippery from other causes (x:false, y:true), since slippery roads do not imply rain (y->x)
# simplifies to (true->false), which is false
props.append(C16)

# 17. X → Y ⊢ ¬Y → ¬X
# As proposition in PL: ((X -> Y) -> (¬Y -> ¬X)
C17 = Implies(Implies(X, Y), Implies(Not(Y), Not(X)))
props.append(C17)

# 18. ¬(X ∨ Y) ↔ ¬X ∧ ¬Y
# As proposition in PL: (¬(X ∨ Y) -> (¬X ∧ ¬Y)) /\ ((¬X ∧ ¬Y) -> ¬(X ∨ Y))
C18 = And(Implies(Not(Or(X, Y)), And(Not(X), Not(Y))), Implies(And(Not(X), Not(Y)), Not(Or(X, Y))))
props.append(C18)

# 19. ¬(X ∧ Y) ↔ ¬X ∨ ¬Y
# As proposition in PL: (¬(X ∧ Y) -> (¬X ∨ ¬Y)) /\ ((¬X ∨ ¬Y) -> ¬(X ∧ Y))
C19 = And(Implies(Not(And(X, Y)), Or(Not(X), Not(Y))), Implies(Or(Not(X), Not(Y)), Not(And(X, Y))))
props.append(C19)

s = Solver()
i = 0

for item in props:
    s.reset()
    if i == 6:
        i += .1
    elif (i == 6.1):
        i += .9
    else:
        i += 1
    s.add(Not(item))
    if (s.check() == unsat):
        print("proposition", int(i), "is valid")
    else:
        print("proposition", int(i), "is not valid, counterexample:", s.model())


