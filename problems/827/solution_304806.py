from math import sqrt
def qtd_divisores(n):
    '''Funcao que conta o numero de divisores de um determinado numero'''
    for i in range (1, n):
        if n % i == 0:
             return i + 1
        return n