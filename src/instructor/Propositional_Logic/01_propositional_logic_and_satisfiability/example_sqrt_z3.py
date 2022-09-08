from unicodedata import name
from z3 import *

def sqrt(n):
    sqrtn = Real('sqrtn')
    s = Solver()
<<<<<<< HEAD
    s.add(And((sqrtn ** 2) == n), sqrtn >= 0) # replace True with required declarative spec
    isSat = s.check()
    if (isSat == sat) :
        return s.model()
    return -1
    
print(sqrt(64))


def neg_sqrt(n) :
    sqrtn = Real('sqrtn')
    s = Solver()
    s.add(And((sqrtn ** 2) == n), sqrtn <= 0) # replace True with required declarative spec
    isSat = s.check()
    if (isSat == sat) :
        return s.model()
    return -1

print(neg_sqrt(17))
=======
    # replace True with required declarative spec
    s.add(And(sqrtn**2 == n, sqrtn >= 0))
    isSat = s.check()
    if (isSat == sat):
        return s.model()
    return -1


print(sqrt(17))
>>>>>>> 200f99da54a1d070f2daee7229a034bdcc195915
