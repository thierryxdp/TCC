def filtra_pares(a, b, c, d):
    lista = []

    if a / 2 == int(a / 2):
        f = (a,)
    if b / 2 == int(b / 2):
        g = (b,)
    if c / 2 == int(c / 2):
        z = (c,)
    if d / 2 == int(d / 2):
        e = (d,)

    return f + g + z + e