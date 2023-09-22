def filtra_pares(a,b,c,d):
    a1=a%2
    b1=b%2
    c1=c%2
    d1=d%2
    if a1==0 and b1==0 and c1==0 and d1==0:
        return (a,b,c,d)
    elif a1==0 and b1==0 and c1==0 and not d1==0:
        return (a,b,c)
    elif a1==0 and b1==0 and not c1==0 and d1==0:
        return (a,b,d)
    elif a1==0 and not b1==0 and c1==0 and d1==0:
        return (a,c,d)
    elif not a1==0 and b1==0 and c1==0 and d1==0:
        return (b,c,d)
    elif a1==0 and b1==0 and not c1==0 and not d1==0:
        return (a,b)
    elif a1==0 and not b1==0 and not c1==0 and d1==0:
        return (a,d)
    elif a1==0 and not b1==0 and c1==0 and not d1==0:
        return (a,c)
    elif not a1==0 and b1==0 and not c1==0 and d1==0:
        return (b,d)
    elif not a1==0 and b1==0 and c1==0 and not d1==0:
        return (b,c)
    elif not a1==0 and not b1==0 and c1==0 and d1==0:
        return (c,d)
    elif a1==0 and not b1==0 and not c1==0 and not d1==0:
        return (a,)
    elif not a1==0 and b1==0 and not c1==0 and not d1==0:
        return (b,)
    elif not a1==0 and not b1==0 and c1==0 and not d1==0:
        return (c,)
    else:
        if not a1==0 and not b1==0 and not c1==0 and d1==0:
            return (d,)