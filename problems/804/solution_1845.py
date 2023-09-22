def filtra_pares(t):

    x,y,z,w=t

    a = x%2
    b = y%2
    c = z%2
    d = w%2
    
    if a==0 and b==0 and c==0 and d==0:
        return (x,y,z,w)
    elif a==0 and b==0 and c==0:
        return (x,y,z)
    elif a==0 and b==0:
        return (x,y)
    elif a==0 and c==0 and d==0:
        return (x,z,w)
    elif a==0 and c==0:
        return (x,z)
    elif a==0 and d==0:
        return (x,w)
    elif a==0:
        return (x,)
    elif b==0 and c==0 and d==0:
        return (y,z,w)
    elif b==0 and c==0:
        return (y,z)
    elif b==0 and d==0:
        return (y,w)
    elif b==0:
        return (y,)
    elif c==0 and d==0:
        return (z,w)
    elif c==0:
        return (z,)
    elif d==0:
        return (w,)
    else:
        return ()