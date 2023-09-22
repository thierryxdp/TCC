def faltante (lista):
    '''Dada uma lista com N - 1 inteiros numerados de 1 a N,
    retorne com o número inteiro faltante;
    list -> int'''
    list.sort (lista)
    if 1 not in lista:
        return 1
    if lista [-1] < len(lista) + 1:
        return len(lista) + 1
    i = 0
    falt = 0
    while i < len(lista) - 1:
        if lista[i + 1] - lista[i] > 1:
            falt = falt + lista[i] + 1
        i = i + 1
    return falt + 1