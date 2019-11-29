import math
import re

def pourcent(chaine, sequence):
    longueur = len(sequence)
    nbtime = chaine.count(sequence)
    return (longueur*nbtime) / len(chaine) * 100


c: str = input("Chaîne : ")
while not re.match("^[atgc]*$", c):
    c: str = input("Chaîne : ")

s: str = input("Séquence : ")
while not re.match("^[atgc]*$", s):
    s: str = input("Séquence : ")

print(pourcent(c, s))
