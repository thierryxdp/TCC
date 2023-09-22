import math

def bolos(a,b,c):
    z=a/2
    x=b/3
    w=c/5
    "O cálculo será realizado utlizando a divisão dos ingredientes que o João possui pela quantidade mínima de cada elemento necessário."
    return math.floor(min(z,x,w))