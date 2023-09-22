def filtra_pares(q,w,e,r):
    a=q%2
    s=w%2
    d=e%2
    f=r%2
    if a==0 and s==1 and d==1 and f==1 :
        return (q)
    elif a==0 and s==0 and d==1 and f==1:
        return (q,w)
    elif a==0 and s==0 and d==0 and f==1:
        return (q,w,e)
    elif a==0 and s==1 and d==0 and f==0:
        return (q,w,e,r)
    elif a==1 and s==0 and d==1 and f==1:
        return (w)
    elif a==1 and s==0 and d==0 and f==1:
        return (w,e)
    elif a==1 and s==0 and d==0 and f==0:
        return (w,e,r)
    elif a==1 and s==1 and d==0 and f==1:
        return (e)
    elif a==1 and s==1 and d==0 and f==0:
        return (e,r)
    elif a==1 and s==1 and d==1 and f==0:
        return (r)
    else :
        return ()