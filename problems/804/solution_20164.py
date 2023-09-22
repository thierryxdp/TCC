def filtra_pares(tuple):
    '''Retorna os valores pares da tupla'''
    return filter(lambda x: int(x)%2 == 0, tuple)