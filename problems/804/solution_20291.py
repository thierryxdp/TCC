def filtra_pares(tupla):
    '''Analisa e retorna uma tupla apenas com os números pares da tupla t
    	tuple->tuple'''
    
    t=()
    
    if tupla[0]%2==0:
        t=t+(tupla[0],)
    
    if tupla[1]%2==0:
        t=t+(tupla[1],)
        
    if tupla[2]%2==0:
        t=t+(tupla[2],)
        
    if tupla[3]%2==0:
        t=t+(tupla[3],)
        
    	return t
    
    else:
        return t