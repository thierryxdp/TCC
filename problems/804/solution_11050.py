def filtra_pares(tup):
    '''função que retorna uma nova tupla somente com elementos pares; tupla -> tupla'''
    if not tup:
        return 0
    par = (tup[0] % 2 == 0)
    if par:
        return filtra_pares(tup[1:])