def filtra_pares((a,b,c,d)):
    t=()
    if a%2==0:
        t=t+(filtra_pares[0],)
    if b%2==0:
        t=t+(filtra_pares[1],)
    if c%2==0:
        t=t+(filtra_pares[2],)
    if d%2==0:
        t=t+(filtra_pares[3],)
    return t