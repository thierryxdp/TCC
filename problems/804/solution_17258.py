def filtra_pares(inteiros):
    a = inteiros[0]
    b = inteiros[1]
    c = inteiros[2]
    d = inteiros[3]
    resp = ( )
    if a%2==0:
        resp = resp + a
    if b%2==0:
        resp = resp + b
    if c%2==0:
        resp = resp + c
    if d%2==0:
        resp = resp + d
    return resp