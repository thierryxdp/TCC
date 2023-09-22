def filtra_pares(tup):
    '''função que retorna uma nova tupla somente com elementos pares; tupla -> tupla'''
    if not t:
        return 0
    par = (tup[0] % 2 == 0)
    if par:
        return 1 + filtra_pares(tup[1:])
    else:
        return filtra_pares(tup[1:])