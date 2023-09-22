def filtra_pares (tupla):
    '''...'''
    T = ()
    if tupla[0]%2 == 0:
        T = T + (tupla[0],)
    if tupla[1]%2 == 0:
        T = T + (tupla[1],)
    if tupla[2]%2 == 0:
        T = T + (tupla[2],)
    if tupla[3]%2 == 0:
        T = T + (tupla[3],)
        
        return T