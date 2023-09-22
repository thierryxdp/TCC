def filtra_pares(a,b,c,d):
    """funcao que retorna uma tupla formada por inteiros pares da tupla original;
    float, float, float, float -> float"""
    if a%2==0 and b%2!=0 and c%2!=0 and d%2!=0:
        return (a)
    elif a%2==0 and b%2==0 and c%2!=0 and d%2!=0:
        return (a,b)
    elif a%2==0 and b%2!=0 and c%2==0 and d%2!=0:
        return (a,c)
    elif a%2==0 and b%2!=0 and c%2!=0 and d%2==0:
        return (a,d)
    elif a%2==0 and b%2==0 and c%2==0 and d%2!=0:
        return (a,b,c)
    elif a%2==0 and b%2==0 and c%2!=0 and d%2==0:
        return (a,b,d)
    elif a%2==0 and b%2!=0 and c%2==0 and d%2==0:
        return (a,c,d)
    elif (a%2!=0 and b%2==0) and (c%2==0 and d%2==0):
        return (b,c,d)
    elif a%2!=0 and b%2==0 and c%2!=0 and d%2!=0:
        return (b)
    elif a%2!=0 and b%2==0 and c%2==0 and d%2!=0:
        return (b,c)
    elif a%2!=0 and b%2==0 and c%2!=0 and d%2==0:
        return (b,d)
    elif a%2!=0 and b%2!=0 and c%2==0 and d%2!=0:
        return (c)
    elif a%2!=0 and b%2!=0 and c%2==0 and d%2==0:
        return (c,d)
    elif a%2!=0 and b%2!=0 and c%2!=0 and d%2==0:
        return (d)
    elif a%2==0 and b%2==0 and c%2==0 and d%2==0:
        return (a,b,c,d)