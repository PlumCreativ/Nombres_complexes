from math import *
from typing import get_type_hints

a = float(input("Rentrer le nombre réel de la fonction z: "))
b = float(input("Rentrer le nombre imaginaire de la fonction z: "))
c = complex(a, b)

d = float(input("Rentrer le nombre réel de la fonction z': "))
f = float(input("Rentrer le nombre imagibnaire de la fonction z: "))
e = complex(d, f)

print("")
print(f"La fonction complex de z est: {c}\nLa fonction conjugué est: {c.conjugate()}")
print(f"La fonction complex de z' est: {e}\nLa fonction conjugué est: {e.conjugate()}")
print("")
print(f"L'ensemble de fonctions est: {c + e} \nL'esnsemble de la fonction z est: {a + b} \nL'ensemble de la fontion z' est: {d + f}")
print("")

print("Fin du programme !")
