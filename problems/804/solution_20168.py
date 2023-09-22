def filtra_pares(numeros):
    '''Retorna os valores pares da tupla;
    tuple -> tuple'''
    return tuple(filter(lambda x: int(x)%2 == 0, numeros))