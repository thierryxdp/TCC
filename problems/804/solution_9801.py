def filtra_pares(t):
    '''Função que dado uma tupla t, contendo 4 elementos inteiros, retorne outra tupla apenas com 
    os elementos pares de t
    tup -> tup'''
    TupVazia = ()
    if t[0] % 2 == 0:
        TupVazia += (t[0],)
    if t[1] % 2 == 0:
        TupVazia += (t[1],)
    if t[2] % 2 == 0:
        TupVazia += (t[2],)
    if t[3] % 2 == 0:
        TupVazia += (t[3],)
    return TupVazia