import math

def bolos(a,b,c):
    xicara=(a//2)
    ovo=(b//3)
    colher=(c//5)
    return math.floor((xicara+ovo+colher)/3)
"""retorna a quantidade máxima de bolos que é possível fazer dada a quantidade de ingredientes disponiveis dividida pela quantidade necessária.
int,int,int -> int"""