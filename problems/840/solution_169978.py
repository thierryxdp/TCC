from math import floor
def bolos(a,b,c):
    x = floor(a/2)
    o = floor(b/3)
    l = floor(c/5)
    return min(x,o,l)