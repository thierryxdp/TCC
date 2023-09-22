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
        filtro = filtro + (tupla[0],)
    if tupla[1]%2==0:
        filtro = filtro + (tupla[1],)
    if tupla[2]%2==0:
        filtro = filtro + (tupla[2],)
    if tupla[3]%2==0:
        filtro = filtro + (tupla[3],)
    
    return tupla