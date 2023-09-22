def filtra_pares(x):
    nt = ()
    if x[0] % 2 == 0:
        x[0] += nt
    if x[1] % 2 == 0:
        x[1] += nt
    if x[2] % 2 == 0:
        x[2] += nt
    if x[3] % 2 == 0:
        x[3] += nt
        return nt