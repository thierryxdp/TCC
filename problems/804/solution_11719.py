def par(n):
    """Decifra se o numero é par"""
    return (n % 2) == 0
def impar(n):
    """Decifra se o numero não é par"""
    return not par(n)
def filtra_pares(t):
    """Filtra os elemntos pares de uma tupla"""
    ret = ()
    if par(t[0]):
        ret = ret + (t[0],)
    if par(t[1]):
        ret = ret + (t[1],)
    if par(t[2]):
        ret = ret + (t[2],)
    if par(t[3]):
        ret = ret + (t[3],)
    return ret