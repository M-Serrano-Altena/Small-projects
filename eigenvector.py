# Marc Serrano Altena
# 07-12-2022
# Dit programma geeft bij een 2 x 2 matrix de eigenwaarden met de bijbehorende eigenvectoren

import numpy as np
import sympy as sp
from polynomial import *

# TODO: 3x3 laten werken met complexe getallen

def matrix_2x2():
    A = np.array([['a','c'], ['b','d']])
    print(f"A =")
    print(A)
    print(f"Voer bij matrix A de a, b, c en d in.")

    a = sp.nsimplify(complex(input("a = ")))
    b = sp.nsimplify(complex(input("b = ")))
    c = sp.nsimplify(complex(input("c = ")))
    d = sp.nsimplify(complex(input("d = ")))

    x = sp.Symbol('x')
    eigenwaarde_1, eigenwaarde_2 = quadratic(1, -(a+d), a*d - b*c)

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
    global counter
    counter = 0

    A = np.array([['a','d', 'g'], ['b','e', 'h'], ['c', 'f', 'i']])
    print("A = ")
    print(A)
    print("Voer bij matrix A alle waardes in.")

    a = sp.nsimplify(complex(input("a = ")))
    b = sp.nsimplify(complex(input("b = ")))
    c = sp.nsimplify(complex(input("c = ")))
    d = sp.nsimplify(complex(input("d = ")))
    e = sp.nsimplify(complex(input("e = ")))
    f = sp.nsimplify(complex(input("f = ")))
    g = sp.nsimplify(complex(input("g = ")))
    h = sp.nsimplify(complex(input("h = ")))    
    i = sp.nsimplify(complex(input("i = ")))

    eigenwaarde_1, eigenwaarde_2, eigenwaarde_3 = cubic(1, -(a + e + i), (a*e + a*i + e*i - b*d - c*g - f*h),  - (a*e*i - a*f*h - b*d*i + b*f*g + c*d*h - c*e*g))
    print(f"De eigenwaardes zijn {eigenwaarde_1}, {eigenwaarde_2} en {eigenwaarde_3}.")

    def eigenvector(eigenwaarde):
        global counter
        nul_vector = np.array([[0], [0], [0]])
        eigenvector = np.array([[sp.nsimplify(g*(eigenwaarde - e) + d*h)], [sp.nsimplify(h*(eigenwaarde - a) + b*g)], [sp.nsimplify((eigenwaarde - a)*(eigenwaarde - e) - b*d)]])

        if np.array_equal(eigenvector, nul_vector):
            eigenvector = np.array([[sp.nsimplify(d*(eigenwaarde - i) + f*g)], [sp.nsimplify((eigenwaarde - a)*(eigenwaarde - i) - c*g)], [sp.nsimplify(f*(eigenwaarde - a) + c*d)]])
        
        if np.array_equal(eigenvector, nul_vector):
            eigenvector = np.array([[sp.nsimplify((eigenwaarde - e)*(eigenwaarde -i) - f*h)], [sp.nsimplify(b*(eigenwaarde - i) + h*c)], [sp.nsimplify(c*(eigenwaarde - e) + b*f)]])

        if np.array_equal(eigenvector, nul_vector):
            counter += 1

            if counter == 1:
                eigenvector = np.array([[sp.nsimplify(-d)], [sp.nsimplify(a - eigenwaarde)], [sp.nsimplify(0)]])

            if counter == 2:
                eigenvector = np.array([[sp.nsimplify(-g)], [sp.nsimplify(0)], [sp.nsimplify(a - eigenwaarde)]])

        if np.array_equal(eigenvector, nul_vector):

            if counter == 1:
                eigenvector = np.array([[sp.nsimplify(1)], [sp.nsimplify(0)], [sp.nsimplify(0)]])
            
            if counter == 2:
                eigenvector = np.array([[sp.nsimplify(0)], [sp.nsimplify(1)], [sp.nsimplify(0)]])
            
            if counter == 3:
                eigenvector = np.array([[sp.nsimplify(0)], [sp.nsimplify(0)], [sp.nsimplify(1)]])

        eigenvector = eigenvector * 1/np.amin(eigenvector[np.nonzero(eigenvector)])

        return eigenvector

    eigenvector_1 = eigenvector(eigenwaarde_1)
    eigenvector_2 = eigenvector(eigenwaarde_2)
    eigenvector_3 = eigenvector(eigenwaarde_3)

    print(f"Bij de eigenwaarde {eigenwaarde_1} hoort eigenvector:")
    print(f"{eigenvector_1}")
    print(f"Bij de eigenwaarde {eigenwaarde_2} hoort eigenvector:")
    print(f"{eigenvector_2}")
    print(f"Bij de eigenwaarde {eigenwaarde_3} hoort eigenvector:")
    print(f"{eigenvector_3}")
    
matrix_size = 0
while matrix_size != 2 and matrix_size != 3:
    matrix_size = int(input(f"Is de matrix 2x2 (voer in: 2) of 3x3 (voer in: 3): "))

if matrix_size == 2:
    matrix_2x2()

elif matrix_size == 3:
    matrix_3x3()