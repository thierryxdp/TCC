import math
def qtd_divisores(num):
    '''função que retorna os divisores de um número'''
    '''int-->int'''
    resultado=0
    if num<0:
        return 0
    for i in range(1,int(num/2+1)):
        if num%i==0:
            resultado=resultado+1
    return resultado+1