def filtra_pares (a,b,c,d):
    '''filtragem recebe uma tupla com quatro elementos inteiros e devolve os elementos pares da tupla original, na mesma ordem em que se encontravam.
    int,int,int,int--> int'''
    a1=(abs(a))%2
    b1=(abs(b))%2
    c1=(abs(c))%2
    d1=(abs(d))%2
    if a1==0 and b1==0 and c1==0 and d1==0:
        return (a,b,c,d,)
    elif a1==0 and b1==0 and c1==0:
        return (a,b,c,)
    elif a1==0 and b1==0:
        return (a,b,)
    elif a1==0:
        return(a,)
    elif a1==0  and c1==0:
        return (a,c,)
    elif a1==0  and d1==1:
        return (a,d,)
    elif b1==0:
        return (b,)
    elif b1==0 and c1==0:
        return (b,c,)
    elif b1==0 and d1==0:
        return (b,d,)
    elif c1==0:
        return (c,)
    elif c1==0 and d1==0:
        return (c,d,)
    elif d1==0:
        return (d,)
    else:
        return ( )