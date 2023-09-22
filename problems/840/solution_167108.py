import math
def bolos(a,b,c):
    a=math.floor(a/2);
    b=math.floor(b/3);
    c=math.floor(c/5);
    return min(a,b,c)