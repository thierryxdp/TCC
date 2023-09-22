import math

def bolos(A,B,C):
    xic=math.floor(A/2)
    ovo=math.floor(B/3)
    col=math.floor(C/5)
    if xic<=ovo and xic<=col:
        return xic
    if ovo<=xic and ovo<=col:
        return ovo
    return col