def faltante(L):
    '''Dada uma lista com N - 1 inteiros numerados de 1 a N, descobre qual o
número inteiro desse intervalo está faltando.'''
    valores = sorted(L)
    i = 0
    while i < len(L):
        if i + 1 != valores:
            return i + 1

    return len(valores)+1