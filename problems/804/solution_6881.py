def filtra_pares(a,b,c,d):
    todos = ((a),(b),(c),(d))
    pares = ()
    if a %2==0:
        return str(pares) + a
    if b %2==0:
        return str(pares) + b
    if c %2==0:
        return str(pares) + c
    if d %2==0:
        return str(pares) + d
    else:
        return ' '