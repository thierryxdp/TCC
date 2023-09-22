import math
def qtd_divisores(n):
    '''função que calcula e retorna a quantidade de divisores que um numero n tem.int->int'''
    divisores = [1]
    if n <= 0:
        return 0
    for i in range(2,int(math.sqrt(n))+1):
        if numero % i == 0:
            divisores.extend([i,n/i])
    divisores.extend([n])
    lista = list(set(divisores))
    return len(lista)