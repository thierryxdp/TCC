def filtra_pares(tupla):
    '''Função que ao receber uma tupla com quatro elementos
    retorna uma nova tupla com apenas os elementos pares da
    tupla original na mesma ordem da tupla recebida.
    tuple -> tuple'''
    tuplaN= ()
    if tupla[0] % 2 == 0:
        tuplaN = tuplaN + (tupla[0],)
    if tupla[1] % 2 == 0:
        tuplaN = tuplaN + (tupla[1],)
    if tupla[2] % 2 == 0:
        tuplaN= tuplaN + (tupla[2],)
    if tupla[3] % 2 ==0:
        tuplaN = tuplaN + (tupla[3],)
    
    return tuplaN