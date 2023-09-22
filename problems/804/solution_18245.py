def filtra_pares(n):
    pares = ()
    if n[0] % 2 == 0:
        pares = pares + (n[0], )
    if n[1] % 2 == 0:
        pares = pares + (n[1], )
    if n[2] % 2 == 0:
        pares = pares + (n[2], )
    if n[3] % 2 == 0:
        pares = pares + (n[3], )
    return pares