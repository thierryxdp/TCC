def filtra_pares(t):
    t2 = ()
    if t[0]%2 == 0:
        a = t[0],
        t2 = t2 + a
    if t[1]%2 == 0:
        b = t[1],
        t2 = t2 + b
    if t[2]%2 == 0:
        c = t[2],
        t2 = t2 + c
    if t[3]%2 == 0:
        d = t[3],
        t2 = t2 + d
    return t2