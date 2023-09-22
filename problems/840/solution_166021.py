import math
def bolos(a,b,c):
    xicara=math.floor(a/2)
    ovo=math.floor(b/3)
    colher=math.floor(c/5)
    return min(xicara,ovo,colher)
"""retorna a quantidade máxima de bolos que é possível fazer dada a quantidade de ingredientes disponíveis dividido pela quantidade da receita.
int,int,int -> int"""