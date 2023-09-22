def filtra_pares(tupla):
    a = tupla[0]
    b = tupla[1]
    c = tupla[2]
    d = tupla[3]
    pares = ()
    if a%2==0:
        pares+=(a,)
    if b%2==0:
        pares+=(b,)
    if c%2==0:
        pares+=(c,)
    if d%2==0:
        pares+=(d,)
    return pares