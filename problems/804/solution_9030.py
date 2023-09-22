def filtra_pares(a, b, c, d):
    r = ()
    if a % 2 == 0:
        r.append(a)
    if b % 2 == 0:
        r.append(b)
    if c % 2 == 0:
        r.append(c)
    if d % 2 == 0:
        r.append(d)
    return r