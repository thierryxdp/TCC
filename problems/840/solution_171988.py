import math

def bolos(a,b,c):
    f=(a/2)
    o=(b/3)
    l=(c/5)
def menor(f,o,l):
    min = f
    if o < min:
        min = o
    if l < min:
        min = l
    return min

	print(menor(f,o,l))
    print()