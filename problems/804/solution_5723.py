def filtra_pares (tup):
    """..."""
    x = tup[0] % 2
    y= tup[1] % 2
    z= tup[2] % 2
    w = tup[3] % 2
    if x == 0 and y == 0 :
        return tup[0], tup [1]
    if x == 0 and z == 0 :
        return tup[0], tup[2]
    if x == 0 and w == 0:
        return tup[0],tup[3]
    if y == 0 and z== 0:
        return tup[1], tup[2]
    if y == 0 and w == 0:
        return tup[1],tup[3]
    if z == 0 and w == 0:
        return tup[2],tup[3]
    if x == 0 and y == 0 and z == 0:
        return tup[0],tup[1],tup[2]
    if x == 0 and y == 0 and w == 0:
        return tup[0],tup[1],tup[3]
    if x == 0 and z == 0 and w == 0:
        return tup[0],tup[2],tup[3]
    if y == 0 and z == 0 and w == 0:
        return tup[1] ,tup[2], tup[3]