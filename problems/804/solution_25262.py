def filtra_pares(x):
    '''Função que retorne uma nova tupla contendo apenas
    os elementos pares da tupla original, na mesma ordem
    em que se encontravam. tuple -> tuple'''
    pares = ()
    if (x[0]%2) == 0:
        pares = pares + ([0],)
    if (x[1]%2) == 0:
        pares = pares + (x[1],)
    if (x[2]%2) == 0:
        pares = pares + (x[2],)
    if (x[3]%2) == 0:
        pares = pares + (x[3],)
        return pares