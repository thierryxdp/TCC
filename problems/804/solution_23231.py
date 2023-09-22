def filtra_pares(x):
    t = tuple(x)
    i = t[:1]
    i2 = t[1:2]
    i3 = t[2:3]
    i4 = t[3:]

    j = (str(i))
    k = j.replace("(","")
    l = k.replace(")","")
    m = l.replace(",","")
    a = int(m)

    j2 = (str(i2))
    k2 = j2.replace("(","")
    l2 = k2.replace(")","")
    m2 = l2.replace(",","")
    b = int(m2)

    j3 = (str(i3))
    k3 = j3.replace("(","")
    l3 = k3.replace(")","")
    m3 = l3.replace(",","")
    c = int(m3)

    j4 = (str(i4))
    k4 = j4.replace("(","")
    l4 = k4.replace(")","")
    m4 = l4.replace(",","")
    d = int(m4)
    
    filtro =()

    if a%2 == 0:
        filtro = (a,)
    if b%2 == 0:
        filtro = filtro + (b,)
    if c%2 == 0:
        filtro = filtro + (c,)
    if d%2 == 0:
        filtro = filtro + (d,)
    return filtro