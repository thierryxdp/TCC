def filtra_pares(t,v,q,w):
    if not t:
        return 0

    par = (t[0] % 2 == 0)

    if par:
        return 1 + filtra_pares(t[1:])
    else:
        return filtra_pares(t[1:])