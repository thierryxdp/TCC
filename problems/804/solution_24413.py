def filtra_pares(a,b,c,d):
    '''Retorne uma nova tupla contendo apenas os elemntos pares
    da tupla original, na mesma ordem em que se encontravam.
    tuple -> tuple'''
    a,b,c,d = ((a%2) == 0, (b%2) == 0, (c%2) == 0,(d%2) == 0)
    x = a,b,c,d
    tuple = x
    return (x.count(True))