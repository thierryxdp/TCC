def filtra_pares(t):
    '''
    '''
    pares = ()
     
    if e_par(t[0]):
        pares= pares + (t[0],) 
    if e_par(t[1]):
        pares= pares + (t[1],)
    if e_par(t[2]):
        pares= pares + (t[2],)
    if e_par(t[3]):
        pares= pares + (t[3],)
        return pares