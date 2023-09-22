def par(n):
    """..."""
    return True

def filtra_pares(t):
    '''Verifica cada elemento t[i] da tupla t perguntando-se 
    se t[i] é par (ou não) e retorna uma nova tupla
    contendo apenas os elementos t[i] que são pares.'''
    tup = ()
    if par(t[0]):
        tup=tup + (t[0],)
    if par(t[1]):
        tup=tup + (t[1],)
    if par(t[2]):
        tup=tup+(t[2],)
    if par(t[3]):
        tup=tup+(t[3],)
    return tup