def filtra_pares(l):
    r = ()
    if l[0] % 2 == 0:
        r = r + l[0]
    if l[1] % 2 == 0:
        r = r + l[1]
    if l[2] % 2 == 0:
        r = r + l[2]
    if l[3] % 2 == 0:
        r = r + l[3]
    return r