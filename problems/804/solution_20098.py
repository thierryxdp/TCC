def filtra_pares(x):
    a,b,c,d = x
    if a%2==0:
        return (a,)
    if b%2==0:
        return (b,)
    if c%2==0:
        return (c,)
    if d%2==0:
        return (d)
    if a%2==0 and b%2 ==0:
        return (a, b)
    elif a%2==0 and c%2 ==0:
        return (a, c)
    elif b%2==0 and c%2 ==0:
        return (b, c)
    elif a%2==0 and b%2 ==0 and c%2 ==0:
        return (a, b, c)