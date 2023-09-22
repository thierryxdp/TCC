def filtra_pares(x):
    (a, b, c, d) = x
    nova_tupla = ()
    if a%2 == 0:
        return nova_tupla(()) + tuple(x[0])
    if b%2 == 0:
        return nova_tupla(()) + x[1]
    if c%2 == 0:
        return nova_tupla(()) + x[2]
    if d%2 == 0:
        return nova_tupla(()) + x[3]
    return nova_tupla