def filtra_pares(x):
    a, b, c, d = x
    if a%2 == 0:
        return a
    elif b%2 == 0:
        return b
    else:
        return ()
    if c%2 == 0:
        return c
    else:
        return ()
    if d%2 == 0:
        return d
    else:
        return ()
    return x