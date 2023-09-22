from math import sqrt
def qtd_divisores(n):
    '''função que dado um numero(n), retorna quantos divisores
    n tem;int->int'''
    resp=0
    for i in range(1, n//2+1):
        if n % i == 0:
            resp+=1 
    return resp