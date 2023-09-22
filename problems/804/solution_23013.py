def filtra_pares(a, b, c, d):
    if a%2 == 0:
        filtro = (a,)
    if b%2 == 0:
        filtro = filtro + (b,)
    if c%2 == 0:
        filtro = filtro + (c,)
    if d%2 == 0:
        filtro = filtro + (d,)
    return filtro