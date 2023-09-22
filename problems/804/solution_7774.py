def filtra_pares(tupla):
    '''
    retorna tupla de pares
    parâmetros
    	a,b,c,d:int
    saída
    	tuple(int)
    '''
    
    filtro = ()
    if tupla[0]%2==0:
        filtro = filtro + (a,)
    if tupla[1]%2==0:
        filtro = filtro + (b,)
    if tupla[2]%2==0:
        filtro = filtro + (c,)
    if tupla[3]%2==0:
        filtro = filtro + (d,)
    
    return tupla