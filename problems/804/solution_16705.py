#Start your python function here
def filtra_pares(a,b,c,d):
    """Seleciona apenas os inteiros pares da tupla dada, e os retorna em tupla"""
    """tuple-> tuple"""
    if a%2==0 and b%2==0 and c%2==0 and d%2==0:
        return (a,b,c,d)
    elif a%2==0:
        return (a,)
    elif b%2==0:
        return (b,)
    elif c%2==0:
        return (c,)
    elif d%2==0:
        return (d,)
    elif a%2==0 and b%2==0:
        return (a,b,)
    elif b%2==0 and c%2==0:
        return (b,c,)
    elif c%2==0 and d%2==0:
        return (c,d,)
    elif a%2==0 and c%2==0:
        return (a,c,)
    elif a%2==0 and d%2==0:
        return (a,d,)
    elif a%2==0 and c%2==0:
        return (b,d,)
    elif a%2==0 and b%2==0 and c%2==0:
        return (a,b,c,)
    elif b%2==0 and c%2==0 and d%2==0:
        return (b,c,d,)
    elif a%2==0 and c%2==0 and d%2==0:
        return (a,c,d,)
    elif a%2==0 and b%2==0 and d%2==0:
        return (a,b,d,)
    else:
        return ()