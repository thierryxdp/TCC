def filtra_pares(L):
    x=tuple(L)
    s=x[0]
    t=x[1]
    r=x[2]
    q=x[3]
    a=s%2
    b=t%2
    c=r%2
    d=q%2
    if a==0 and b==0 and c==0 and d==0:
        return (s,t,r,q)
    elif a==0 and b==0 and c==0:
        return (s,t,r)
    elif a==0 and b==0 and d==0:
        return (s,t,q)
    elif b==0 and c==0 and d==0:
        return (t,r,q)
    elif a==0 and b==0:
        return (s,t)
    elif a==0 and c==0:
        return (s,r)
    elif a==0 and d==0:
        return (s,q)
    elif b==0 and c==0:
        return (t,r)
    elif b==0 and d==0:
        return (t,q)
    elif c==0 and d==0:
        return (r,q)
    elif a==0:
        return (s,)
    elif b==0:
        return (t,)
    elif c==0:
        return (r,)
    elif d==0:
        return (q,)
    else:
        return tuple()