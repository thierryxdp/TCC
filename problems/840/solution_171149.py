from math import floor


def bolos(a,b,c):
    return floor(ingredientes(a,b,c))

def ingredientes (a,b,c):
    return min(a/2,b/3,c/5)