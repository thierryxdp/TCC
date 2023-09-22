from math import*
def bolos(a,b,c):
    if a<2 or b<3 or c<5:
        return 0
    elif a<b<c:
        return floor(c/2)
    elif a<c<b:
        return a/2
    elif b<c<a:
        return b/3
    elif b<a<c:
        return b/3
    elif c<a<b:
        return c/5
    elif c<b<a:
        return c/5