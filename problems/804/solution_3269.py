def filtra_pares(tup):
    a = tup[0]
    b = tup[1]
    c = tup[2]
    d = tup[3]
    
    if a%2==0 and b%2==0 and c%2==0 and d%2==0:
        return (a,)+(b,)+(c,)+(d,)
    elif a%2==0 and b%2==0 and c%2==0:
        return (a,)+(b,)+(c,)
    elif a%2==0 and b%2==0:
        return (a,)+(b,)
    elif a%2==0 and c%2==0:
        return (a,)+(c,)
     elif a%2==0 and d%2==0:
        return (a,)+(d,)
    elif  b%2==0 and c%2==0:
        return (b,)+(c,)
    elif  b%2==0 and d%2==0:
        return (b,)+(d,)
    elif c%2==0 and d%2==0:
        return (c,)+(d,)