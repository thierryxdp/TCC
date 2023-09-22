def filtra_pares (x):
    if x[1] % 2 == 0 and x[0] % 2 == 0:
        return x[0], x[1]
    if x[2] % 2 == 0 and x[3] % 2 == 0:
        return x[2], x[3]