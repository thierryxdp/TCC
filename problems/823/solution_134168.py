def faltante(L):
    '''Recebe uma lista com N - 1 inteiros numerados de
    1 a N e retorna qual é o número inteiro desse
    intervalo que está faltando
    list -> int'''
    i = 1
    while i < len(L):
        if L[i + 1] != L[i] + 1:
            faltante = L[i] + 1
        i += 1
    return faltante