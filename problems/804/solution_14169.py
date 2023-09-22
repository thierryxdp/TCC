def filtra_pares(x):
    a,b,c,d = x
    y = ()
    if a%2==0:
        y = y+(a,)
    if b%2==0:
        y = y+(b,)
    if c%2==0:
        y = y+(c,)
    if d%2==0:
        y = y+(d,)
    return y