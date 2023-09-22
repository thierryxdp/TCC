def faltante(L):
    """ dada uma lista com N-1 inteiros numerados de 1 a N, a função retorna o número
    inteiro desse intervalo que está faltando;
    list->int"""
    indice=1
    numerofaltante=0
    list.sort(L)
    while indice <=(len(L)-1):
        if L[indice]-L[indice-1]==1:
            numerofaltante
        if L[indice]-L[indice-1]==2:
            numerofaltante=L[indice]-1
        indice=indice+1
    return numerofaltante