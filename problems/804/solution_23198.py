def filtra_pares(x):
    t = tuple(x)
    j = str(t)
    s = j.replace(",","")
    y = s.replace(")","")
    h = y.replace("(","")
    a = int(h[:1])
    b = int(h[2:3])
    c = int(h[4:5])
    d = int(h[6:])
    if a%2 == 0:
        filtro = (a,)
    if b%2 == 0:
        filtro = filtro + (b,)
    if c%2 == 0:
        filtro = filtro + (c,)
    if d%2 == 0:
        filtro = filtro + (d,)
    return filtro