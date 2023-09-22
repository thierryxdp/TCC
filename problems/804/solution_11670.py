def filtra_pares(a,b,c,d):
    """Retorna apenas os elementos pares da tupla
    int, int, int, int"""
    # se todos forem pares
    if a%2==0 and b%2==0 and c%2==0 and d%2==0:
        return a,b,c,d
    # se apenas um for par
    elif a%2==0 and b%2!=0 and c%2!=0 and d%2!=0:
        return a
    elif elif a%2!=0 and b%2==0 and c%2!=0 and d%2!=0:
        return b
    elif a%2!=0 and b%2!=0 and c%2==0 and d%2!=0:
        return c
    elif a%2!=0 and b%2!=0 and c%2!=0 and d%2==0:
        return d
    # se dois forem pares
    elif a%2==0 and b%2==0 and c%2!=0 and d%2!=0:
        return a,b
    elif a%2==0 and b%2!=0 and c%2==0 and d%2!=0:
        return a,c
    elif a%2==0 and b%2!=0 and c%2!=0 and d%2==0:
        return a,d
    elif a%2!=0 and b%2==0 and c%2==0 and d%2!=0:
        return b,c
    elif a%2!=0 and b%2==0 and c%2!=0 and d%2==0:
        return b,d
    elif a%2!=0 and b%2!=0 and c%2==0 and d%2==0:
        return c,d
    # se três forem pares
    elif a%2==0 and b%2==0 and c%2==0 and d%2!=0:
        return a,b,c
    elif a%2==0 and b%2==0 and c%2!=0 and d%2==0:
        return a,b,d
    elif a%2!=0 and b%2==0 and c%2==0 and d%2==0:
        return b,c,d
    elif a%2==0 and b%2!=0 and c%2==0 and d%2==0:
        return a,c,d