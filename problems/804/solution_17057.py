def par(n):
    return n%2==0
def filtra_pares(p):
    pares = ()
    if par(p[0]):
        pares = pares + (p[0],)
    if par(p[1]):
        pares = pares + (p[1],)
    if par(p[2]):
        pares = pares + (p[2],)
    if par(p[3]):
        pares = pares + (p[3],)
    return pares