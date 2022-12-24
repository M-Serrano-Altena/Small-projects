# Marc Serrano Altena
# 23-12-2022
# gives the solution to a quadratic and cubic equation

# TODO: laten werken voor complexe oplossingen
# 'better comments' checken?

import sympy as sp


def int_check(num):
    if sp.im(num) == 0 and sp.re(num) % 1 == 0:
        return int(sp.re(num))
    return num


def quadratic(a, b, c):
    x1 = int_check(1/(2*a)*(-b + sp.sqrt(b**2 - 4*a*c)))
    x2 = int_check(1/(2*a)*(-b - sp.sqrt(b**2 - 4*a*c)))
    return x1, x2


def cubic(a, b, c):
    w = -1/2 + 1/2*sp.sqrt(3)*1j
    p = b - (a**2)/3
    q = c + (2 * a**3)/27 - (b*a)/3

    u = sp.nsimplify(sp.cbrt(-q/2 + sp.sqrt((q**2)/4 + (p**3)/27)))
    v = sp.nsimplify(sp.cbrt(-q/2 - sp.sqrt((q**2)/4 + (p**3)/27)))

    if sp.simplify(3*u*v + p) == 0:
        x1 = sp.simplify(u + v - a/3)
        x2 = sp.simplify(u * w + v * w**2 - a/3)
        x3 = sp.simplify(u * w**2 + v * w - a/3)

    elif sp.simplify(3*u*v*w + p) == 0:
        x1 = sp.simplify(u + v * w - a/3)
        x2 = sp.simplify(u * w + v - a/3)
        x3 = sp.simplify(u * w**2 + v * w**2 - a/3)

    elif sp.simplify(3*u*v*w**2 + p) == 0:
        x1 = sp.simplify(u + v * w**2 - a/3)
        x2 = sp.simplify(u * w + v * w - a/3)
        x3 = sp.simplify(u * w**2 + v - a/3)

    else:
        print("Er is iets mis gegaan")

    return sp.nsimplify(x1), sp.nsimplify(x2), sp.nsimplify(x3)

x1, x2, x3 = cubic(1, 1, 1)
print("The solutions to the cubic equation are:")
print(f"x1 = {x1}")
print(f"x2 = {x2}")
print(f"x3 = {x3}")
