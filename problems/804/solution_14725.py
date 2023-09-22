def filtra_pares (t):
    if not t:
        return 0

    par = (t[0] % 2 == 0)

    if par:
        return filtra_pares
    else:
        return filtra_pares(t[1:])