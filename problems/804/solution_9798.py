def filtra_pares(t):
    '''Função que dado uma tupla t, contendo 4 elementos inteiros, retorne outra tupla apenas com 
    os elementos pares de t
    tup -> tup'''
    TupVazia = ()
    if t[0] % 2 == 0:
        TupVazia += (t[0],)
    elif t[1] % 2 == 0:
        TupVazia += (t[1],)
    elif t[3] % 2 == 0:
        TupVazia += (t[3],)
    elif t[3] % 2 == 0:
        TupVazia += (t[3],)
    return TupVazia