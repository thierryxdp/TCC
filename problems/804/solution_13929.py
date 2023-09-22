def filtra_pares(x):
    if x[0] % 2 == 0:
        return x[0]
    elif x[2] % 2 == 0:
        return x[1]
    else:
        if x[0] % 2 == 0 and x[2] % 2 == 0:
            return x[0], x[2]