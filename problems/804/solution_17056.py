def par(n):
    return n%2==0
def filtra_pares(p):
    pares = ()
    if par(t[0]):
        pares = pares + (p[0],)
    if par(t[1]):
        pares = pares + (p[1],)
    if par(t[2]):
        pares = pares + (p[2],)
    if par(t[3]):
        pares = pares + (p[3],)
    return pares