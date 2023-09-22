def filtra_pares(x):
    """A função apartir de uma tupla com quatro elementos inteiros retorna uma outra tupla 
    com apenas elementos pares".tuple--tuple""""
    a,b,c,d=x
    f=a%2
    i=b%2
    l=c%2
    t=d%2
    if f==0 and i==0 and l==0 and t==0:
        return (a,b,c,d)
    elif f!=0 and i==0 and l==0 and t==0:
        return (b,c,d)
    elif f==0 and i!=0 and l==0 and t==0:
        return (a,c,d)
    elif f==0 and i==0 and l!=0 and t==0:
        return (a,b,d)
    elif f==0 and i==0 and l==0 and t!=0:
        return (a,b,c)
    elif f!=0 and i!=0 and l==0 and t==0:
        return (c,d)
    elif f!=0 and i==0 and l!=0 and t==0:
        return (b,d)
    elif f!=0 and i==0 and l==0 and t!=0:
        return (b,c)
    elif f==0 and i!=0 and l!=0 and t==0:
        return (a,d)
    elif f==0 and i!=0 and l==0 and t!=0: 
        return (a,c)
    elif f==0 and i==0 and l!=0 and t!=0:
        return (a,b)
    elif f==0 and i!=0 and l!=0 and t!=0:
        return (a,)
    elif f!=0 and i==0 and l!=0 and t!=0:
        return (b,)
    elif f!=0 and i!=0 and l==0 and t!=0:
        return (c,)
    elif f!=0 and i!=0 and l!=0 and t==0:
        return (d,)
    else:
        return ()