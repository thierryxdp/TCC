def filtra_pares(t):
    a=t[0]
    b=t[1]
    c=t[2]
    d=t[3]
    r=()
    if a%2==0:
        r=(a,)
    if b%2==0:
        r=r+(b,)
    if c%2==0:
        r=r+(c,)
    if d%2==0:
        r=r+(d,)
    return r