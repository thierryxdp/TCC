def filtra_pares(tup):
    '''função que retorna uma nova tupla somente com elementos pares; tupla -> tupla'''
    if tup == ():
        return 0
    else:
        return tup[0] + filtra_pares(tup[1:])