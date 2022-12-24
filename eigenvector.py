# Marc Serrano Altena
# 07-12-2022
# Dit programma geeft bij een 2 x 2 matrix de eigenwaarden met de bijbehorende eigenvectoren

import numpy as np
import sympy as sp

def int_check(num):
    if sp.im(num) == 0 and sp.re(num) % 1 == 0:
        return int(sp.re(num))
    return num

def matrix_2x2():
    A = np.array([['a','c'], ['b','d']])
    print(f"A =")
    print(A)
    print(f"Voer bij matrix A de a, b, c en d in.")

    a = int_check(complex(input("a = ")))
    b = int_check(complex(input("b = ")))
    c = int_check(complex(input("c = ")))
    d = int_check(complex(input("d = ")))

    x = sp.Symbol('x')
    eigenwaarde_1, eigenwaarde_2 = sp.solve(x**2 - (a+d)*x + a*d - b*c)

    if b != 0:
        eigenvector_1 = np.array([[eigenwaarde_1 - d], [b]])
        eigenvector_2 = np.array([[eigenwaarde_2 - d], [b]])

    elif c != 0:
        eigenvector_1 = np.array([[c], [eigenwaarde_1 - a]])
        eigenvector_2 = np.array([[c], [eigenwaarde_2 - a]])

    else:
        eigenvector_1 = np.array([[1], [0]])
        eigenvector_2 = np.array([[0], [1]])

    print(f"De eigenwaardes zijn {eigenwaarde_1} en {eigenwaarde_2}.")
    print(f"Bij de eigenwaarde {eigenwaarde_1} hoort de eigenvector:")
    print(eigenvector_1)
    print(f"Bij de eigenwaarde {eigenwaarde_2} hoort de eigenvector:")
    print(eigenvector_2)


def matrix_3x3():
    A = np.array([['a','d', 'g'], ['b','e', 'h'], ['c', 'f', 'i']])
    print("A = ")
    print(A)
    print("Voer bij matrix A alle waardes in.")

    a = int_check(complex(input("a = ")))
    b = int_check(complex(input("b = ")))
    c = int_check(complex(input("c = ")))
    d = int_check(complex(input("d = ")))
    e = int_check(complex(input("e = ")))
    f = int_check(complex(input("f = ")))
    g = int_check(complex(input("g = ")))
    h = int_check(complex(input("h = ")))    
    i = int_check(complex(input("i = ")))

    x = sp.Symbol('x')
    eigenwaarde_1, eigenwaarde_2, eigenwaarde_3 = sp.solve(x**3 - (a + e + i)*x**2 + (a*e + a*i + e*i - b*d - c*g - f*h)*x - (a*e*i - a*f*h - b*d*i + b*f*g + c*d*h - c*e*g))
    print(f"De eigenwaardes zijn {eigenwaarde_1}, {eigenwaarde_2} en {eigenwaarde_3}.")
    

matrix_3x3()