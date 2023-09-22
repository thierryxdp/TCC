import math
def qtd_divisores(numero):
    '''Função que conta quantos divisores um número tem.'''
    '''int->int'''
    divisores = [1]
    if numero <=0:
        return 0
    for i in range(2,int(math.sqrt(numero))+1):
        if numero % i == 0:
            divisores.extend([i,numero/i])
    divisores.extend([numero])
    lista = list(set(divisores))
    return len(lista)