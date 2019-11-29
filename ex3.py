import math

e: float = 0
for i in range(0, 50):
    e += 1/math.factorial(i)

f: float = 2.71828182845905523536

print("e = " + str(e))
print("différence e et f : " + str(f-e))
