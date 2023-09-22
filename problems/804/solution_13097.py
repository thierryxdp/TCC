def filtra_pares(tupla):
    '''função que recebe uma tupla de 4 elementos
    inteiros e retorna uma nova tupla apenas com os 
    elementos pares da tupla original.
    tupla-->tupla'''
    
    tuplaN = ()
    if tupla[0] % 2 == 0:
        tuplaN = tuplaN + (tupla[0],)
    if tupla[1] % 2 == 0:
        tuplaN = tuplaN + (tupla[1],)
    if tupla[2] % 2 == 0:
        tuplaN = tuplaN + (tupla[2],)
    if tupla[3] % 2 == 0:
        tuplaN = tuplaN + (tupla[3],)
    return tuplaN