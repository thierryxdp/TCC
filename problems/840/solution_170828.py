def bolos(A,B,C):
    import math
    a = math.floor(A/2)
    b = math.floor(B/3)
    c = math.floor(C/5)
    lista = [a,b,c]
    return min(lista)