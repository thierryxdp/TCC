def filtra_pares(t):

    resultado = ()
    s = int(t[0])
    b = int(t[1])
    p = int(t[2])
    c = int(t[3])

    if s%2==0:
        resultado = resultado + (s,)

    if b%2==0:
        resultado = resultado + (b,)

    if p%2==0:
        resultado = resultado + (p,)

    if c%2==0:
        resultado = resultado + (c)

    return resultado