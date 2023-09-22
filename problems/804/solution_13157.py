def filtra_pares(t):
    par = (t[0] % 2 == 0)
    if par:
        return 1 + filtra_pares(t[1:])
    else:
        return filtra_pares(t[1:])