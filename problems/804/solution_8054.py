def filtra_pares(a,b,c,d):
    """Dado uma tupla com quatro elementos inteiros como parâmetro,
    retorna apenas os elementos pares dessa tupla, na mesma ordem;
    tuple->tuple"""
    x=a%2
    y=b%2
    z=c%2
    w=d%2
    if x!=0:
        return (b,c,d)
    elif x!=0 and y!=0:
        return (c,d)
    elif x!=0 and y!=0 and z!=0:
        return (d,)
    elif x!=0 and y!=0 and z!=0 and w!=0:
        return ()
    elif y!=0:
        return (a,c,d)
    elif y!=0 and z!=0:
        return (a,d)
    elif y!=0 and z!=0 and w!=0:
        return (a,)
    elif z!=0:
        return (a,b,d)
    elif z!=0 and x!=0:
        return (b,d)
    elif z!=0 and w!=0:
        return (a,b)
    elif z!=0 and x!=0 and w!=0:
        return (b,)
    elif z!=0 and y!=0 and w!=0:
        return (x,)
    elif z!=0 and y!=0 and x!=0:
        return (w,)
    elif w!=0:
        return (a,b,c)
    elif w!=0 and z!=0:
        return (a,b)
    elif w!=0 and x!=0:
        return (b,c)
    elif w!=0 and y!=0:
        return (a,c)