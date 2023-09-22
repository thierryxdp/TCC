def filtra_pares(a,b,c,d):
    '''função que recebe os valores a,b,c e d e retorna os pares, int, int-->int'''
    pares=tuple()
    
    if a%2==0:
        pares+=(a,)
        
    if b%2==0:
    	pares+=(b,)
        
    if c%2==0:
    	pares+=(c,)
        
    if d%2==0:
    	pares+=(d,)
        
        
    return pares