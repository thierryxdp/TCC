from math import sqrt
def qtd_divisores(n):
    '''função que dado um numero(n), retorna quantos divisores
    n tem;int->int'''
    resp=[]
    for i in range(1, n//1+1):
        if n % i == 0:
            resp+=str(i) 
    return len(resp)