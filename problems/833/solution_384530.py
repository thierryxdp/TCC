def conta_numero(numero,matriz):
    '''Dado um numero inteiro e uma matriz, conta quantas vezes o numero aparece na matriz.int,list(list)->int'''
    i=0
    j=0
    while i<len(matriz):
        j=matriz[i].count(numero)+j
        i=i+1
    return j