def filtra_pares(tupla):
    """retorna uma tupla contendo apenas
    os elementos pares e na mesma ordem
    de uma outra tupla de quatro elementos
    passada como parametro.
    tup -> tup"""
    pares = ()
    if tupla[0] % 2 == 0:
        pares = pares + (tupla[0],)
    if tupla[1] % 2 == 0:
        pares = pares + (tupla[1],)
    if tupla[2] % 2 == 0:
        pares = pares + (tupla[2],)
    if tupla[3] % 2 == 0:
        pares = pares + (tupla[3],)
    return pares