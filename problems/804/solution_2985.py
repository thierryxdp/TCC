def filtra_pares(a,b,c,d):
    x = a%2
    w = b%2
    z = c%2
    y = d%2
    if x==0 and w==0 and z==0 and y==0:
        return (a,b,c,d)
    elif x==0 and w==0 and z==0:
        return (a,b,c)
    elif x==0 and w==0 and y==0:
        return (a,b,d)
    elif x==0 and z==0 and y==0:
        return (a,c,d)
    elif x==0 and y==0:
        return (a,d)
    elif x==0 and w==0:
        return (a,b)
    elif x==0 and z==0:
        return (a,c)
    elif w==0 and y==0:
        return (b,d)
    elif z==0 and y==0:
        return (c,d)
    elif w==0 and z==0:
        return (b,c)
    elif x==0:
        return (a)
    elif y==0:
        return (b)
    elif z==0:
        return (c)
    elif y==0:
        return (d)
    else:
        return ()