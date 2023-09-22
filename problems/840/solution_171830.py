import math
def bolos (a,b,c):
    a=a/2
    b=b/3
    c=c/5
    if a<=b and a<=c:
        return math.floor(a)
    else:
        if b<=a and b<=c:
            return math.floor(b)
        else:
            return math.floor(c)