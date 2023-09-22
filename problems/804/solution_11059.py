def filtra_pares(tup):
    '''função que retorna uma nova tupla somente com elementos pares; tupla -> tupla'''
    0,1,2,3 = tup
    par = (tup[0] % 2 == 0) 
    return filtra_pares(tup[0:])