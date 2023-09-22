def filtra_pares(t):
    '''Essa função tem como objetivo  filtrar os números pares de ama tupla'''
    '''int,int = tupla'''
    tpares = tuple()

	if (t[0]%2) == 0:
        tpares = tpares + (t[0],)
    if (t[1]%2) == 0:
        tpares = tpares + (t[1],)
    if (t[2]%2) == 0:
        tpares = tpares + (t[2],)
    if (t[3]%2) == 0:
        tpares = tpares + (t[3],)
        
    return tpares