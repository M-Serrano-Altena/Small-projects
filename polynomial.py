# Marc Serrano Altena
# 23-12-2022
# gives the solution to a quadratic and cubic equation

# TODO: de sqrt en cbrt funties laten werken met imaginaire getallen 
# 'better comments' checken?

import sympy as sp
import fractions

def int_check(num):
    if sp.im(num) == 0 and sp.re(num) % 1 == 0:
        return int(sp.re(num))
    return num


def sqrt(num):
    num = fractions.Fraction(num).limit_denominator()

    if '/' in str(num):
        num1, num2 = str(num).split('/')
        num1, num2 = int_check(float(num1)), int_check(float(num2))
        print(num1, num2)
        num = sp.sqrt(num1)/sp.sqrt(num2)
    
    else:
        num = sp.sqrt(num)
    
    return num


def cbrt(num):
    print("hello world")    
    num = fractions.Fraction(num).limit_denominator()

    if '/' in str(num):
        num1, num2 = str(num).split('/')
        num1, num2 = int_check(float(num1)), int_check(float(num2))
        print(num1, num2)
        num = sp.cbrt(num1)/sp.sqrt(num2)
    
    else:
        num = sp.cbrt(num)
    
    return num

def quadratic(a,b,c):
    x1 = int_check(1/(2*a)*(-b + sp.sqrt(b**2 - 4*a*c)))
    x2 = int_check(1/(2*a)*(-b - sp.sqrt(b**2 - 4*a*c)))
    return x1, x2

def cubic(a,b,c):
    w = -1/2 + 1/3*sp.sqrt(3)*1j
    p = b - (a**2)/3
    q = c + (2 * a**3)/27 - (b*a)/3

    u = sp.cbrt(-q/2 + sp.sqrt((q**2)/4 + (p**3)/27))
    v = sp.cbrt(-q/2 - sp.sqrt((q**2)/4 + (p**3)/27))

    print(cbrt(sqrt((q**2)/4 + (p**3)/27)))


    print(sp.simplify(3*u*v + p)) 

    if 3 * u * v + p == 0:
        x1 = u + v - a/3
        x2 = u * w + v * w**2 - a/3
        x3 = u * w**2 + v * w - a/3

    elif 3 * u * v * w + p == 0:
        x1 = u + v * w - a/3
        x2 = u * w + v - a/3
        x3 = u * w**2 + v * w**2 - a/3

    elif 3 * u * v * w**2 + p == 0:
        x1 = u + v * w**2 - a/3
        x2 = u * w + v * w - a/3
        x3 = u * w**2 + v - a/3
    
    else:
        print("Er is iets mis gegaan")
    
    return x1, x2, x3

print(cubic(-6, 11, -6))