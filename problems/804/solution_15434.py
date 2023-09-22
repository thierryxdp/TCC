def filtra_pares(x):
    pares = ()
    if x[0]%2==0:
        pares = pares + (x[0],)
    if x[1]%2==0:
        pares = pares + (x[1],)
    if x[2]%2==0:
        pares = pares + (x[2],)
    if x[4]%2==0:
        pares = pares + (x[3],)
    return pares