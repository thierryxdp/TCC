def filtra_pares(x):
    """"""
    a,b,c,d=x
    if a%2==0:
        pares=a
    if b%2==0:
        pares=pares+b
    if c%2==0:
        pares=pares+c
    if d%2==0:
        pares=pares+d
    return pares