def filtra_pares(l):
    r = ()
    a = (l[0],)
    b = (l[1],)
    c = (l[2],)
    d = (l[3],)
    if l[0] % 2 == 0:
        r = r + a
    if l[1] % 2 == 0:
        r = r + b
    if l[2] % 2 == 0:
        r = r + c
    if l[3] % 2 == 0:
        r = r + d
    return r