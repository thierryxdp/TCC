def filtra_pares(t):
    '''
    '''
    
    pares = ()
     
    if (t[0])%2==0:
        pares= pares + (t[0],) 
        return pares
    if (t[1])%2==0:
        pares= pares + (t[1],)
        return pares
    if (t[2])%2==0:
        pares= pares + (t[2],)
        return pares
    if (t[3])%2==0:
        pares= pares + (t[3],)
        return pares
    
    else:
        return ()