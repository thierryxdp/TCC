filtra_pares(tupla,):
    '''retorna os elementos pares de uma tupla de quatro elementos que foi recebida
    tuple->tuple'''
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