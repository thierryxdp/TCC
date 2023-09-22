def filtra_pares(tup):
    '''analisa os quatro elementos da tupla original, retornando uma nova tupla somente com os números pares
    str -> str'''
    pares = ()
    if tup[0]%2 == 0:
        pares += (tup[0],)
    if tup[1]%2 == 0:
        pares += (tup[1],)
    if tup[2]%2 == 0:
        pares += (tup[2],)
    if tup[3]%2 == 0:
        pares += (tup[3],)
    return pares