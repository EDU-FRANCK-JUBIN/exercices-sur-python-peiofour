import math

def getDivisors(n):
    l = []
    for i in range(1, n):
        if n % i == 0:
            l.append(i)
    if len(l) == 1 & l[0] == 1:
        print("C'est un nombre premier !")
    else:
        print("Diviseurs de " + str(n) + " : " + str(l))


foo = int(input("Entrez votre entier strictement positif : "))
getDivisors(foo)
