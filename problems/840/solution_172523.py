import math

def bolos(A,B,C):
    #calculos da quandidade de cada item
    xic=math.floor(A/2)
    ovo=math.floor(B/3)
    col=math.floor(C/5)
    #verifica qual é o menor dos itens, resultando na quantidade máxima de bolos
    if xic<=ovo and xic<=col:
        return xic
    if ovo<=xic and ovo<=col:
        return ovo
    return col