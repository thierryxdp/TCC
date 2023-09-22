def filtra_pares (tup):
    """..."""
    x = tup[0] % 2
    y= tup[1] % 2
    z= tup[2] % 2
    w = tup[3] % 2
    if x == 0 and y == 0 :
        return tup[0:1]
    if y == 0:
        return tup[1]
    if z == 0:
        return tup[2]
    if w == 0:
        return tup[3]