# Be sure you've done pip install z3-solver
from z3 import *


# Here's a file you can often copy as a starting 
# point on a working program to solve some problem
# of interest. Here the problem is to compute and
# return a non-negative square root of argument, n 
def shape(n):
    
    
    # Create z3 variable(s) representing the unknown
    # Here, the unknown, x, is the square root of n.
    t = Real('triangle')
    s = Real('square')
    c = Real('circle')
    
    # Important: This is where you express what
    # values count as solutions using propositional
    # logic, but in the slightly different syntax
    # of Z3 expressions.
    C1 = (t + s + c == 10)# a solution squared must be n
    C2 = (c + s - t == 6)       # and must also be non-negative
    C = And(C1, C2) # combine using logical "and"
    C3 = (c + t - s == 4)
    CC = And(C, C3)
    
    
    # Create a Z3 "SMT" solver object, and give it 
    # the overall constraint to be solved, here C.
    s = Solver()
    s.add(CC)
    
    # Run the Z3 model finder, capturing "sat"
    # or "unsat" as the return value 
    isSat = s.check()
    
    # If there's a model/solution return it 
    if (isSat == sat):
        return s.model()
    # otherwise return inconsistent value for error
    return -1

# Set up and run the function and report its results
n = 17
s = shape(n)
if (s == -1) :
    print("There is no combination")
else :
    print("The corresponding shape values are:", s)
