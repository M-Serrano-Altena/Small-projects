# Marc Serrano Altena
# 23-12-2022
# gives the solution to a quadratic and cubic equation
# --> sympy.solve() 

# TODO: laten werken voor complexe oplossingen

import sympy as sp


def int_check(num):
    if sp.im(num) == 0 and sp.re(num) % 1 == 0:
        return int(sp.re(num))
    return num


def quadratic(a, b, c):
    x1 = int_check(1/(2*a)*(-b + sp.sqrt(b**2 - 4*a*c)))
    x2 = int_check(1/(2*a)*(-b - sp.sqrt(b**2 - 4*a*c)))
    return x1, x2


def cubic(a, b, c, d):
    w = -1/2 + 1/2*sp.sqrt(3)*1j
    p = (3*a*c - b**2)/(3*a**2)
    q = (2*b**3 - 9*a*b*c + 27*a**2*d)/(27*a**3)

    u = sp.nsimplify(sp.cbrt(-q/2 + sp.sqrt((q**2)/4 + (p**3)/27)))
    v = sp.nsimplify(sp.cbrt(-q/2 - sp.sqrt((q**2)/4 + (p**3)/27)))

    if round(sp.re(sp.simplify(3*u*v + p)), 10) == 0 and round(sp.im(sp.simplify(3*u*v + p)), 10) == 0:
        x1 = round(sp.re(sp.simplify(u + v - b/(3*a))), 10) + round(sp.im(sp.simplify(u + v - b/(3*a))), 10)*1j
        x2 = round(sp.re(sp.simplify(u*w**2 + v*w - b/(3*a))), 10) + round(sp.im(sp.simplify(u*w**2 + v*w - b/(3*a))), 10)*1j
        x3 = round(sp.re(sp.simplify(u*w + v*w**2 - b/(3*a))), 10) + round(sp.im(sp.simplify(u*w + v*w**2 - b/(3*a))), 10)*1j

    elif round(sp.re(sp.simplify(3*u*v*w + p)), 10) == 0 and round(sp.im(sp.simplify(3*u*v*w + p)), 10) == 0:
        x1 = round(sp.re(sp.simplify(u + v*w - b/(3*a))), 10) + round(sp.im(sp.simplify(u + v*w - b/(3*a))), 10)*1j
        x2 = round(sp.re(sp.simplify(u*w + v - b/(3*a))), 10) + round(sp.im(sp.simplify(u*w + v - b/(3*a))), 10)*1j
        x3 = round(sp.re(sp.simplify(u*w**2 + v*w**2 - b/(3*a))), 10) + round(sp.im(sp.simplify(u*w**2 + v*w**2 - b/(3*a))), 10)*1j

    elif round(sp.re(sp.simplify(3*u*v*w**2 + p)), 10) == 0 and round(sp.im(sp.simplify(3*u*v*w**2 + p)), 10) == 0:
        x1 = round(sp.re(sp.simplify(u + v*w**2 - b/(3*a))), 10) + round(sp.im(sp.simplify(u + v*w**2 - b/(3*a))), 10)*1j
        x2 = round(sp.re(sp.simplify(u*w + v*w - b/(3*a))), 10) + round(sp.im(sp.simplify(u*w + v*w - b/(3*a))), 10)*1j
        x3 = round(sp.re(sp.simplify(u*w**2 + v- b/(3*a))), 10) + round(sp.im(sp.simplify(u*w**2 + v - b/(3*a))), 10)*1j

    else:
        x1, x2, x3 = 'error'
        print("Er is iets mis gegaan")

    return sp.nsimplify(x1), sp.nsimplify(x2), sp.nsimplify(x3)

x1, x2, x3 = cubic(1, 1, 1, 1)
print("The solutions to the cubic equation are:")
print(f"x1 = {x1}")
print(f"x2 = {x2}")
print(f"x3 = {x3}")