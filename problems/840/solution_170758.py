import math
def bolos(a,b,c):
    x=math.floor(a/2)
    y=math.floor(b/3)
    z=math.floor(c/5)
    lista=(x,y,z)
    menor=min(lista)
    return menor