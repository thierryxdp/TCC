def filtra_pares(x):
    '''função que filtra uma tupla com quatro elementos e retorna outra tupla somente com os elementos pares'''
    pares = filter(lambda x: x % 2 == 0, x)
    pares = tuple(pares)
    return pares