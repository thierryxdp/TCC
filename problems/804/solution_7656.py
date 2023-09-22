def filtra_pares(tp):
    par = ()
    a = tp[0]
    b = tp[1]
    c = tp[2]
    d = tp[3]
    if a%2 == 0:
        par = par + (a,)
    if b%2 == 0:
        par = par + (b,)
    if c%2 == 0:
        par = par + (c,)
    if d%2 == 0:
        par = par + (d,)
    return par