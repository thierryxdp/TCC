def filtra_pares(tupla):
    '''Dada uma tupla com quatro elementos inteiros, retorna uma nova tupla contendo apenas os elemtnos pares da tupla original, 
    na mesma ordem em que se encontravam.
    tupla -> tupla'''
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