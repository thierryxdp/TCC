def filtra_pares( T ):
    '''filtra os números pares de uma tupla de tamanho 4'''
    '''tuple -> tuple'''
    
    t = tuple(,)
    
    if T[0] % 2 == 0:
        t = t + tuple(T[0],)
    if T[1] % 2 == 0:
        t = t + tuple(T[1],)
    if T[2] % 2 == 0:
        t = t + tuple(T[2],)
    if T[3] % 2 == 0:
        t = t + tuple(T[3],)
    return t