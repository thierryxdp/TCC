def filtra_pares = (a,b,c,d):
    x = tuple()
    if a%2 == 0: x + tuple(a)
    if b%2 == 0: x + tuple(b)
    if c%2 == 0: x + tuple(c)
    if d%2 == 0: x + tuple(d)
    return x