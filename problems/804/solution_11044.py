def filtra_pares(tup):
    '''função que retorna uma nova tupla somente com elementos pares; tupla -> tupla'''
    if not tup:
        return ()
    par = (tup[()] % 2 == 0)
    if par:
        return 1 + filtra_pares(tup[1:])
    else:
        return filtra_pares(tup[1:])