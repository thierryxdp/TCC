def filtra_pares(t):
    result = ()
    a = int(t[0])
    b = int(t[1])
    c = int(t[2])
    d = int(t[3])
    if a%2 == 0:
        result = result + (a,)
    if b%2 == 0:
        result = result + (b,)
    if c%2 == 0:
        result = result + (c,)
    if d%2 == 0:
        result = result + (d,)
    return result