def f(tupla):
    """Esta é a função que dada uma tupla com 4 elementos inteiros, retorna uma nova tupla apenas com os elementos pares da tupla original,tupla->tupla"""

    a=tupla[0]
    b=tupla[1]
    c=tupla[2]
    d=tupla[3]
     
    if a%2==0 and b%2==0 and c%2==0 and d%2==0:
        return (a,b,c,d)
    
    elif a%2==0 and b%2==0 and c%2==0:
        return (a,b,c)
    
    elif a%2==0 and b%2==0 and d%2==0:
        return (a,b,d)
    
    elif a%2==0 and c%2==0 and d%2==0:
        return (a,c,d)
    
    elif b%2==0 and c%2==0 and d%2==0:
        return (b,c,d)

    elif a%2==0 and b%2==0:
        return (a,b)

    elif a%2==0 and c%2==0:
        return (a,c)

    elif a%2==0 and d%2==0:
        return (a,d)

    elif b%2==0 and c%2==0:
        return (b,c)

    elif b%2==0 and d%2==0:
        return (b,d)

    elif c%2==0 and d%2==0:
        return (c,d)

    elif a%2==0:
        return (a,)

    elif b%2==0:
        return (b,)

    elif c%2==0:
        return (c,)

    elif d%2==0:
        return (d,)
    else:
        return ()