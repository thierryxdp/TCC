def filtra_pares(tup):
    '''função que retorna uma nova tupla somente com elementos pares; tupla -> tupla'''
    pares = ()
    if a[0] % 2 == 0:
        pares = pares + (tup[0],)
    if a[1] % 2 == 0:
        pares = pares + (tup[1],)
    if a[2] % 2 == 0:
        pares = pares + (tup[2],)
    if a[3] % 2 == 0:
        pares = pares + (tup[3],)
    return pares