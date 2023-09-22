def conta_numero(n,m):
    '''Dado um número inteiro e uma matriz,
    conta quantas vezes aquele número aparece na matriz.
    int,list --> int'''
    counter = 0
    for linha in m:
        counter = counter + list.count(linha,n)
    return counter