from math import factorial

def faltante(lista):
    '''Dada uma lista de números inteiros com N-1 números,
    descobre qual número está faltando.
    list -> int'''
    cont = 0
    fat_lista = 1
    while cont < len(lista):
        fat_lista = fat_lista*lista[cont]
    N = max(lista)
    x = factorial(N)//fat_lista
    if x == 1:
        return N+1
    else:
        return x