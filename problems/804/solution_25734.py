def filtra_pares(x):
    nt = ()
    if x[0] % 2 == 0:
        nt += (x[0],)
    if x[1] % 2 == 0:
        nt += (x[1],)
    if x[2] % 2 == 0:
        nt += (x[2],)
    if x[3] % 2 == 0:
        nt += (x[3],)
    return nt