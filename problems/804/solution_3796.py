def filtra_pares(tupla)
    """Recebe quatro números inteiros e retorna apenas os pares.
    tupla(int,int,int,int) -> tupla"""
    a=tupla[0]
    b=tupla[1]
    c=tupla[2]
    d=tupla[3]
    
    if a%2==0 and b%2==0 and c%2==0 and d%2==0:
        return (a,b,c,d)
    elif a%2!=0 and b%2==0 and c%2==0 and d%2==0:
        return (b,c,d)
    elif a%2==0 and b%2!=0 and c%2==0 and d%2==0:
        return (a,c,d)
    elif a%2==0 and b%2==0 and c%2!=0 and d%2==0:
        return (a,b,d)
    elif a%2==0 and b%2==0 and c%2==0 and d%2!=0:
        return (a,b,c)
    elif a%2!=0 and b%2!=0 and c%2==0 and d%2==0:
        return (c,d)
    elif a%2!=0 and b%2==0 and c%2!=0 and d%2==0:
        return (b,d)
    elif a%2!=0 and b%2==0 and c%2==0 and d%2!=0:
        return (b,c)
    elif a%2==0 and b%2!=0 and c%2!=0 and d%2==0:
        return (a,d)
    elif a%2==0 and b%2!=0 and c%2==0 and d%2!=0:
        return (a,c)
    elif a%2==0 and b%2==0 and c%2!=0 and d%2!=0:
        return (a,b)