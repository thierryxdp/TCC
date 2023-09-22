def filtra_pares(a,b,c,d):
    '''
    retorna tupla de pares
    parâmetros
    	a,b,c,d:int
    saída
    	tuple(int)
    '''
    filtro = ()
    if a%2==0:
        filtro = filtro + (a,)
    if b%2==0:
        filtro = filtro + (b,)
    if c%2==0:
        filtro = filtro + (c,)
    if d%2==0:
        filtro = filtro + (d,)
    return filtro