# Marc Serrano Altena
# 07-12-2022
# Dit programma geeft bij een 2x2 en 3x3 matrix de eigenwaarden met de bijbehorende eigenvectoren

import numpy as np
import sympy as sp
from polynomial import *



def matrix_2x2():
    global teller
    teller = 0

    A = np.array([['a','c'], ['b','d']])
    print(f"A =")
    print(A)
    print(f"Voer bij matrix A de a, b, c en d in.")

    a = sp.nsimplify(complex(input("a = ")))
    b = sp.nsimplify(complex(input("b = ")))
    c = sp.nsimplify(complex(input("c = ")))
    d = sp.nsimplify(complex(input("d = ")))

    eigenwaarde_1, eigenwaarde_2 = quadratic(1, -(a+d), a*d - b*c)



    def eigenvector(eigenwaarde):
        global teller

        complx = np.vectorize(complex)
        simplify = np.vectorize(sp.nsimplify)

        teller += 1
        if b != 0:
            eigenvector = np.array([[sp.nsimplify(eigenwaarde - d)], [sp.nsimplify(b)]])

        elif c != 0:
            eigenvector = np.array([[sp.nsimplify(c)], [sp.nsimplify(eigenwaarde - a)]])

        else:
            if teller == 1:
                eigenvector = np.array([[1], [0]])
            
            elif teller == 2:
                eigenvector_2 = np.array([[0], [1]])

        eigenvector = complx(eigenvector)
        eigenvector = eigenvector * 1/np.amin(eigenvector[np.nonzero(eigenvector)])
        eigenvector = simplify(eigenvector)

        return eigenvector
    
    eigenvector_1 = eigenvector(eigenwaarde_1)
    eigenvector_2 = eigenvector(eigenwaarde_2)

    print(f"De eigenwaardes zijn {eigenwaarde_1} en {eigenwaarde_2}.")
    print(f"Bij de eigenwaarde {eigenwaarde_1} hoort de eigenvector:")
    print(eigenvector_1)
    print(f"Bij de eigenwaarde {eigenwaarde_2} hoort de eigenvector:")
    print(eigenvector_2)



def matrix_3x3():
    global counter_mult2, teller
    teller = 0
    counter_mult2 = 0     

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

    eigenvector_1, eigenvector_2, eigenvector_3 = np.array([[0], [0], [0]]), np.array([[0], [0], [0]]), np.array([[0], [0], [0]])

    def eigenvector(eigenwaarde):
        complx = np.vectorize(complex)
        simplify = np.vectorize(sp.nsimplify)

        global counter_mult2, teller
        teller += 1
        nul_vector = np.array([[0], [0], [0]])

        # geo. mult. 1 eigenvectoren
        eigenvector = np.array([[sp.nsimplify(g*(eigenwaarde - e) + d*h)], [sp.nsimplify(h*(eigenwaarde - a) + b*g)], [sp.nsimplify((eigenwaarde - a)*(eigenwaarde - e) - b*d)]])

        if np.array_equal(eigenvector, nul_vector):
            eigenvector = np.array([[sp.nsimplify(d*(eigenwaarde - i) + f*g)], [sp.nsimplify((eigenwaarde - a)*(eigenwaarde - i) - c*g)], [sp.nsimplify(f*(eigenwaarde - a) + c*d)]])
        
        if np.array_equal(eigenvector, nul_vector):
            eigenvector = np.array([[sp.nsimplify((eigenwaarde - e)*(eigenwaarde -i) - f*h)], [sp.nsimplify(b*(eigenwaarde - i) + h*c)], [sp.nsimplify(c*(eigenwaarde - e) + b*f)]])

        # geo. mult. 2 eigenvectoren
        if np.array_equal(eigenvector, nul_vector):
            counter_mult2 += 1

            if counter_mult2 == 1:
                eigenvector = np.array([[sp.nsimplify(-d)], [sp.nsimplify(a - eigenwaarde)], [sp.nsimplify(0)]])

            if counter_mult2 == 2:
                eigenvector = np.array([[sp.nsimplify(-g)], [sp.nsimplify(0)], [sp.nsimplify(a - eigenwaarde)]])
            
            if not np.array_equal(eigenvector, nul_vector) and (np.array_equal(eigenvector * 1/np.amin(eigenvector[np.nonzero(eigenvector)]), eigenvector_1) or np.array_equal(eigenvector * 1/np.amin(eigenvector[np.nonzero(eigenvector)]), eigenvector_2)):
                eigenvector = eigenvector = np.array([[sp.nsimplify(0)], [sp.nsimplify(-g)], [sp.nsimplify(d)]])
        
        if np.array_equal(eigenvector, nul_vector):
            if counter_mult2 == 1:
                eigenvector = np.array([[sp.nsimplify(e - eigenwaarde)], [sp.nsimplify(-b)], [sp.nsimplify(0)]])

            if counter_mult2 == 2:
                eigenvector = np.array([[sp.nsimplify(-h)], [sp.nsimplify(0)], [sp.nsimplify(b)]])

            if not np.array_equal(eigenvector, nul_vector) and (np.array_equal(eigenvector * 1/np.amin(eigenvector[np.nonzero(eigenvector)]), eigenvector_1) or np.array_equal(eigenvector * 1/np.amin(eigenvector[np.nonzero(eigenvector)]), eigenvector_2)):
                eigenvector = eigenvector = np.array([[sp.nsimplify(0)], [sp.nsimplify(-h)], [sp.nsimplify(e - eigenwaarde)]])

        if np.array_equal(eigenvector, nul_vector):
            if counter_mult2 == 1:
                eigenvector = np.array([[sp.nsimplify(i - eigenwaarde)], [sp.nsimplify(0)], [sp.nsimplify(-c)]])

            if counter_mult2 == 2:
                eigenvector = np.array([[sp.nsimplify(f)], [sp.nsimplify(-c)], [sp.nsimplify(0)]])

            if not np.array_equal(eigenvector, nul_vector) and (np.array_equal(eigenvector * 1/np.amin(eigenvector[np.nonzero(eigenvector)]), eigenvector_1) or np.array_equal(eigenvector * 1/np.amin(eigenvector[np.nonzero(eigenvector)]), eigenvector_2)):
                eigenvector = eigenvector = np.array([[sp.nsimplify(0)], [sp.nsimplify(i - eigenwaarde)], [sp.nsimplify(-f)]])

        # geo. mult. 3 eigenvectoren
        if np.array_equal(eigenvector, nul_vector):

            print(f"De eigenwaarde is {eigenwaarde} en de counter is {counter_mult2} en de teller is {teller}")

            if teller == 1:
                eigenvector = np.array([[sp.nsimplify(a)], [sp.nsimplify(b)], [sp.nsimplify(c)]])
            
            if teller == 2:
                eigenvector = np.array([[sp.nsimplify(d)], [sp.nsimplify(e)], [sp.nsimplify(f)]])
            
            if teller == 3:
                eigenvector = np.array([[sp.nsimplify(g)], [sp.nsimplify(h)], [sp.nsimplify(i)]])

        eigenvector = complx(eigenvector)
        eigenvector = eigenvector * 1/np.amin(eigenvector[np.nonzero(eigenvector)])
        eigenvector = simplify(eigenvector)


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


# main program
matrix_size = 0
while matrix_size != 2 and matrix_size != 3:
    matrix_size = int(input(f"Is de matrix 2x2 (voer in: 2) of 3x3 (voer in: 3): "))

if matrix_size == 2:
    matrix_2x2()

elif matrix_size == 3:
    matrix_3x3()