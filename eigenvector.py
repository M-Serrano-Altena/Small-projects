# Marc Serrano Altena
# 07-12-2022
# Dit programma geeft bij een 2 x 2 matrix de eigenwaarden met de bijbehorende eigenvectoren

import numpy as np
import sympy
import fractions

def int_check(num):
    if num % 1 == 0:
        return int(num)
    return num

complx = 0
A = np.array([['a','c'], ['b','d']])
print(f"A =")
print(A)
while complx != "j" and complx != "n":
    complx = input("Zit er in A complexe getallen? j/n: ")

print(f"Voer bij matrix A de a, b, c en d in.")

if complx == "n":
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    d = float(input("d = "))
    a = int_check(a)
    b = int_check(b)
    c = int_check(c)
    d = int_check(d)


elif complx == "j":
    a = complex(input("a = "))
    b = complex(input("b = "))
    c = complex(input("c = "))
    d = complex(input("d = "))



if complx == "n" and 1/4*(a-d)**2 + b*c >= 0:
    eigenwaarde_1 = 1/2 * (a + d) + sympy.sqrt(1/4*(a-d)**2 + b*c)
    eigenwaarde_2 = 1/2 * (a + d) - sympy.sqrt(1/4*(a-d)**2 + b*c)
    eigenwaarde_1 = int_check(eigenwaarde_1)
    eigenwaarde_2 = int_check(eigenwaarde_2)

else:

    square_root = 1/4*(a-d)**2 + b*c
    real = sympy.sqrt(square_root.real)
    imaginairy = fractions.Fraction(square_root.imag)

    if '/' in str(imaginairy):
        imaginairy_1, imaginairy_2 = str(imaginairy).split('/')
    
    else:
        imaginairy_1, imaginairy_2 = imaginairy, 1

    imaginairy = sympy.sqrt(int(imaginairy_1))/sympy.sqrt(int(imaginairy_2))*(1/sympy.sqrt(2) + 1/sympy.sqrt(2)*1j)
    print(real, imaginairy)
    eigenwaarde_1 = sympy.simplify(1/2 * (a + d) + (real + imaginairy))
    eigenwaarde_2 = sympy.simplify(1/2 * (a + d) - (real + imaginairy))

print(eigenwaarde_1)
print(eigenwaarde_2)

if b != 0:
    eigenvector_1 = np.array([[eigenwaarde_1 - d], [b]])
    eigenvector_2 = np.array([[eigenwaarde_2 - d], [b]])
else:
    eigenvector_1 = np.array([[c], [eigenwaarde_1 - a]])
    eigenvector_2 = np.array([[c], [eigenwaarde_2 - a]])

print(f"De eigenwaardes zijn {eigenwaarde_1} en {eigenwaarde_2}.")
print(f"Bij de eigenwaarde {eigenwaarde_1} hoort de eigenvector:")
print(eigenvector_1)
print(f"Bij de eigenwaarde {eigenwaarde_2} hoort de eigenvector:")
print(eigenvector_2)