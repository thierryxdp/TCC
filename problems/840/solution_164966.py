import math
def bolos(a,b,c):
    xf = a/2
    ovo = b/3
    csl = c/5
    bolo = min(xf, ovo, csl)
    return math.floor(bolo)