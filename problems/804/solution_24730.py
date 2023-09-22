def filtra_pares(T):
    '''filtra e retorna numeros pares de uma tupla; tuple-> tuple'''
    
    t=tuple() 
    
    if T[0] % 2 == 0:
        t = t + (T[0],)
    if T[1] % 2 == 0:
        t = t + (T[1],)
    if T[2] % 2 == 0:
        t = t + (T[2],)
    if T[3] % 2 == 0:
        t = t + (T[3],)
    return t