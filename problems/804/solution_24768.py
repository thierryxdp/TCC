def eh_par(num):
    """funcao"""
    return num%2==0


def filtra_pares(t):
    """funcao"""
    pares =()
    
    if eh_par(t[0]):
        pares = pares + (t[0],)
    if eh_par(t[1]):
        pares = pares + (t[1],)
    if eh_par(t[2]):
        pares = pares + (t[2],)
    if eh_par(t[3]):
        pares = pares + (t[3],)
    if eh_par(t[4]):
        pares = pares + (t[4],)
    
    return pares