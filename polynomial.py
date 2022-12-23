# Marc Serrano Altena
# 23-12-2022
# gives the solution to a quadratic and cubic equation
import sympy as sp

def int_check(num):
    if sp.im(num) == 0 and sp.re(num) % 1 == 0:
        return int(sp.re(num))
    return num

def quadratic(a,b,c):
    x1 = int_check(1/(2*a)*(-b + sp.sqrt(b**2 - 4*a*c)))
    x2 = int_check(1/(2*a)*(-b - sp.sqrt(b**2 - 4*a*c)))
    return x1, x2

def cubic():
    pass