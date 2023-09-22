def filtra_pares(a,b,c,d):
    t=()
    p=(a,b,c,d)
    if a%2==0:
        t=t+(p[0],)
    if b%2==0:
        t=t+(p[1],)
    if c%2==0:
        t=t+(p[2],)
    if d%2==0:
        t=t+(p[3],)
    return t