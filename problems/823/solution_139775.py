def faltante(L):
    '''Dada uma lista com N - 1 inteiros numerados de 1 a N, descobre qual o
número inteiro desse intervalo está faltando.'''
    valores = sorted(L)
    N = []
    i = 0
    while i < len(L):
        if i not in valores[i]:
            N = N + [i,]
        else:
            N = N + len(valores) +1
        i += 1

    return N