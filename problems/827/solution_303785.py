import math
def qtd_divisores(num):
    resultado=0
    if num<0:
        return 0
    for i in range(1,int(num/2+1)):
        if num%i==0:
            resultado=resultado+1
    return resultado+1