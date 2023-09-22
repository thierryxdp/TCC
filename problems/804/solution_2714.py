def filtra_pares(tup):
    
    """

    Retorna uma tupla apenas com os elementos pares de tup (tupla com
    4 elementos inteiros)
    
        tup (int,int,int,int) -> tup
        
    Parâmetros:
        tup: tupla com 4 numeros int
    Returns:
        Tupla com os elementos pares da tupla anterior na ordem em que apareceram

    """

    tup = a,b,c,d

    if a % 2 == 0 and b % 2 == 0 and c % 2 == 0 and d % 2 == 0:
        return (a,b,c,d)
    elif a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
        return (a,b,c)
    elif a % 2 == 0 and b % 2 == 0 and d % 2 == 0:
        return (a,b,d)
    elif a % 2 == 0 and c % 2 == 0 and d % 2 == 0:
        return (a,c,d)
    elif a % 2 == 0 and b % 2 == 0:
        return (a,b)
    elif a % 2 == 0 and c % 2 == 0:
        return (a,c)
    elif a % 2 == 0 and d % 2 == 0:
        return (a,d)
    elif a % 2 == 0:
        return (a)
    elif b % 2 == 0 and c % 2 == 0 and d % 2 == 0:
        return (b,c,d)
    elif b % 2 == 0 and c % 2 == 0:
        return (b,c)
    elif b % 2 == 0 and d % 2 == 0:
        return (b,d)
    elif b % 2 == 0:
        return (b)
    elif c % 2 == 0 and d % 2 == 0:
        return (c,d)
    elif c % 2 == 0:
        return (c)
    elif d % 2 == 0:
        return (d)
    else:
        return ( )
        

#Start your python function here