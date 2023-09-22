def filtra_pares(x):
    (a, b, c, d) = x
    nova_tupla = ()
    if a%2 == 0:
        return nova_tupla() + (a,)
    if b%2 == 0:
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
    return x#Start your python function here