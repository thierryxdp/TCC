import math

def bolos(a, b, c):
    a1 = math.floor(a/2)
    b1 = math.floor(b/3)
    c1 = math.floor(c/5)
    return min(a1, b1, c1)