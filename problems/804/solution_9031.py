def filtra_pares(l):
    r = ()
    if l[0] % 2 == 0:
        r.append(l[0])
    if l[1] % 2 == 0:
        r.append(l[1])
    if l[2] % 2 == 0:
        r.append(l[2])
    if l[3] % 2 == 0:
        r.append(l[3])
    return r