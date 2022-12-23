# Marc Serrano Altena
# 07-12-2022
# Dit programma geeft bij een 2 x 2 matrix de eigenwaarden met de bijbehorende eigenvectoren

import numpy as np
import sympy
import fractions
from polynomial import *



complx = 0
A = np.array([['a','c'], ['b','d']])
print(f"A =")
print(A)
print(f"Voer bij matrix A de a, b, c en d in.")

a = int_check(complex(input("a = ")))
b = int_check(complex(input("b = ")))
c = int_check(complex(input("c = ")))
d = int_check(complex(input("d = ")))

square_root = 1/4*(a-d)**2 + b*c
real = sympy.sqrt(square_root.real)
imaginairy = fractions.Fraction(square_root.imag)

if '/' in str(imaginairy):
    imaginairy_1, imaginairy_2 = str(imaginairy).split('/')

else:
    imaginairy_1, imaginairy_2 = imaginairy, 1

imaginairy = sympy.sqrt(int(imaginairy_1))/sympy.sqrt(int(imaginairy_2))*(1/sympy.sqrt(2) + 1/sympy.sqrt(2)*1j)
eigenwaarde_1 = int_check(sympy.simplify(1/2 * (a + d) + (real + imaginairy)))
eigenwaarde_2 = int_check(sympy.simplify(1/2 * (a + d) - (real + imaginairy)))


if b != 0:
    eigenvector_1 = np.array([[eigenwaarde_1 - d], [int_check(sympy.sqrt(b)**2)]])
    eigenvector_2 = np.array([[eigenwaarde_2 - d], [int_check(sympy.sqrt(b)**2)]])

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