def filtra_pares(tup):
    '''função que retorna uma nova tupla somente com elementos pares; tupla -> tupla'''
    par = (tup[0] % 2 == 0) 
    return filtra_pares(tup[0:])