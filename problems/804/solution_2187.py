def filtra_pares(t):

    s = int(t[0])
    b = int(t[1])
    p = int(t[2])
    c = int(t[3])

    if s%2==0:
        resultado1 = (s,)

    if b%2==0:
        resultado2 = (b,)

    if p%2==0:
        resultado3 = (p,)

    if c%2==0:
        resultado4 = (c)

    return (resultado1) + (resultado2) + (resultado3) + (resultado4)