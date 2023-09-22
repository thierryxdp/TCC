def filtra_pares(x):
    '''função que retorna só os elementos pares de determinada tupla
    de 4 parâmetros
    tupla-> tupla'''
    
    a= x[0]
    b= x[1]
    c= x[2]
    d= x[3]
   
    if a%2==0 and b%2==0 and c%2==0 and d%2==0:
        return (a,b,c,d)
    elif a%2==0 and b%2!=0 and c%2!=0 and d%2!=0:
        return (a,)
    elif a%2==0 and b%2==0 and c%2!=0 and d%2!=0:
        return (a,b,)
    elif a%2==0 and b%2==0 and c%2==0 and d%2!=0:
        return (a,b,c,)
    elif a%2==0 and b%2!=0 and c%2==0 and d%2==0:
        return (a,c,d,)
    elif a%2==0 and b%2!=0 and c%2==0 and d%2!=0:
        return (a,c,)
    elif a%2==0 and b%2!=0 and c%2!=0 and d%2==0:
        return (a,d,)
    elif a%2!=0 and b%2==0 and c%2!=0 and d%2!=0:
        return (b,)
    elif a%2!=0 and b%2==0 and c%2==0 and d%2!=0:
        return (b,c,)
    elif a%2!=0 and b%2==0 and c%2==0 and d%2==0:
        return (b,c,d,)
    elif a%2!=0 and b%2==0 and c%2!=0 and d%2==0:
        return (b,d,)
    elif a%2!=0 and b%2!=0 and c%2==0 and d%2!=0:
        return (c,)
    elif a%2!=0 and b%2!=0 and c%2==0 and d%2==0:
        return (c,d,)
    else:
        return ()