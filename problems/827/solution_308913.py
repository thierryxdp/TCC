import math
def qtd_divisores(n):
    ''''''
    cont=0
    for i in range(1,n):
        if n%i==0:
            cont=cont+2
        if i==n:
            cont=cont+1
    return cont