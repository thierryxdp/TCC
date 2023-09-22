def faltante(L):
    '''Dada uma lista com N - 1 inteiros numerados de 1 a N, descobre qual o
número inteiro desse intervalo está faltando.'''
    N = list(range(1, len(L)+2))
    i = 0
    while i <= len(L):
        if N[i] not in L:
            return N[i]
        i += 1