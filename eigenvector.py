# Marc Serrano Altena
# 07-12-2022
# Dit programma geeft bij een 2 x 2 matrix de eigenwaarden met de bijbehorende eigenvectoren

import numpy as np

A = np.array([['a','c'], ['b','d']])
print(f"A =")
print(A)
print(f"Voer bij matrix A de a, b, c en d in.")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
d = float(input("d = "))

def int_check(num):
    if num % 1 == 0:
        return int(num)
    return num

a = int_check(a)
b = int_check(b)
c = int_check(c)
d = int_check(d)

if 1/4*(a-d)**2 + b*c >= 0:
    eigenwaarde_1 = 1/2 * (a + d) + np.sqrt(1/4*(a-d)**2 + b*c)
    eigenwaarde_2 = 1/2 * (a + d) - np.sqrt(1/4*(a-d)**2 + b*c)
    eigenwaarde_1 = int_check(eigenwaarde_1)
    eigenwaarde_2 = int_check(eigenwaarde_2)

else:
    eigenwaarde_1 = complex(1/2 * (a + d), np.sqrt(abs(1/4*(a-d)**2 + b*c)))
    eigenwaarde_2 = complex(1/2 * (a + d), - np.sqrt(abs(1/4*(a-d)**2 + b*c)))


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