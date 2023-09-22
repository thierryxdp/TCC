import random
def faltante(L):
    '''Dada uma lista com N - 1 inteiros numerados de 1 a N, descobre qual o
número inteiro desse intervalo está faltando.'''
    N = []
    x = random.radidnt(1,len(L))
    i = 0
    while i < len(L):
        if L[i] in x:
            N = N + [L[i],]
        i += 1

    return N