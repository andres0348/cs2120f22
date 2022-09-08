from z3 import *

C = Bool('Chase')
D = Bool('Decker')
E = Bool('Ellis')
H = Bool('Heath')
M = Bool('Mullaney')

s = Solver()
s.add(Or(C, D, E, H, M))
s.add(Implies(And(C, Not(H)))D)

