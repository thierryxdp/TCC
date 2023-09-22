def filtra_pares(filtro):
    a=filtro[0]%2
    s=filtro[1]%2
    d=filtro[2]%2
    f=filtro[3]%2
    q=filtro[0]
    w=filtro[1]
    e=filtro[2]
    r=filtro[3]
    if a==0 and s==1 and d==1 and f==1 :
        return (q)
    elif a==0 and s==0 and d==1 and f==1:
        return (q,w)
    elif a==0 and s==0 and d==0 and f==1:
        return (q,w,e)
    elif a==0 and s==0 and d==0 and f==0:
        return (q,w,e,r)
    elif a==1 and s==1 and d==1 and f==0:
        return (r)
    elif a==0 and s==1 and d==0 and f==1:
        return (q,e)
    elif a==0 and s==1 and d==0 and f==0:
        return (q,e,r)
    elif a==0 and s==1 and d==1 and f==0:
        return (q,r)
   
    
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