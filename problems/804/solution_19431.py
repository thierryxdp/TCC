def filtra_pares(a, b, c, d):
    ''
    a1 = a%2
    a2 = b%2
    a3 = c%2
    a4 = d%2
    if a1==0 and a2==0 and a3==0 and a4==0:
        return (a, b, c, d)
    if a1==0 and a2==0 and a3==0:
        return (a, b, c)
    if a1==0 and a2==0:
        return (a, b)
    if a1==0:
        return (a,)