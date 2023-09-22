def bolos(a,b,c):
    import math
    x = math.floor(a/2)
    y = math.floor(b/3)
    z = math.floor(c/5)
    r = min(x,y,z)
    return r