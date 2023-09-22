def filtra_pares(a,b,c,d):
    """funcao que retorna uma tupla so com elementos pares da tupla de entrada;
    tupla de int -> tupla de int"""
    n1=a%2==0
    n2=b%2==0
    n3=c%2==0
    n4=d%2==0
    if n1 and n2 and n3 and n4:
        return (n1,n2,n2,n3,n4)
    elif n1 and n2 and n3:
        return (n1,n2,n3)
    elif n1 and n2 and n4:
        return (n1,n2,n4)
    elif n1 and n3 and n4:
        return (n1,n3,n4)
    elif n2 and n3 and n4:
        return (n2,n3,n4)
    elif n1 and n2:
        return (n1,n2)
    elif n1 and n3:
        return (n1,n3)
    elif n1 and n4:
        return(n1,n4)
    elif n2 and n3:
        return (n2,n3)
    elif n2 and n4:
        return (n2,n4)
    elif n3 and n4:
        return (n3,n4)
    elif n1:
        return (n1)
    elif n2:
        return (n2)
    elif n3:
        return (n3)
    elif n4:
        return (n4)