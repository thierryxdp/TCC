def filtra_pares(x):
    (a, b, c, d) = x
    nova_tupla = ()
    if a%2 == 0:
        return nova_tupla + ((a,))
    if b%2 == 0:
        return nova_tupla + ((a,)) + ((b,))
    if c%2 == 0:
        return nova_tupla + ((a,)) + ((b,)) + ((c,))
    if d%2 == 0:
        return nova_tupla + ((a,)) + ((b,)) + ((c,)) + ((d,))
    return nova_tupla