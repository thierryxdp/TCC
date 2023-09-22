def filtra_pares(N1,N2,N3,N4):
    """funcao que retorna uma tupla so com elementos pares da tupla de entrada;
    tupla de int -> tupla de int"""
    n1=a%2==0
    n2=b%2==0
    n3=c%2==0
    n4=d%2==0
    if n1 and n2 and n3 and n4:
        return (a,b,c,d)
    elif n1 and n2 and n3:
        return (a,b,c)
    elif n1 and n2 and n4:
        return (a,b,d)
    elif n1 and n3 and n4:
        return (a,c,d)
    elif n2 and n3 and n4:
        return (b,c,d)
    elif n1 and n2:
        return (a,b)
    elif n1 and n3:
        return (a,c)
    elif n1 and n4:
        return(a,d)
    elif n2 and n3:
        return (b,c)
    elif n2 and n4:
        return (b,d)
    elif n3 and n4:
        return (c,d)
    elif n1:
        return (a)
    elif n2:
        return (b)
    elif n3:
        return (c)
    elif n4:
        return (d)
    else:
        return ()