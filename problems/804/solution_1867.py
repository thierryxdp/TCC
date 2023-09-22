def filtra_pares([a,b,c,d]):
    S=int(a)
    G=int(b)
    H=int(c)
    I=int(d)
    if S%2==0 and G%2==0 and H%2==0 and I%2==0:
        return (a,b,c,d)
    if S%2!=0 and G%2==0 and H%2==0 and I%2==0:
        return (b,c,d)
    if S%2==0 and G%2!=0 and H%2==0 and I%2==0:
        return (a,c,d)
    if S%2==0 and G%2==0 and H%2!=0 and I%2==0:
        return (a,b,d)
    if S%2==0 and G%2==0 and H%2==0 and I%2!=0:
        return (a,b,c)