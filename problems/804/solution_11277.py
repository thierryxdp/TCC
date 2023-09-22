#Start your python function here
def filtra_pares(a,b,c,d):
    """
    Recebe uma tupla com quatro parametros e retorna uma nova tupla
    contendo apenas os elementos pares da tupla original
    na ordem em que aparecem;
    tupla -> tupla
    """
    if a%2 == 0 and b%2==0:
        return (a,b)
    elif a%2 == 0 and c%2==0:
        return (a,c)
    elif a%2 == 0 and d%2 == 0:
        return (a,d)
    elif b%2 == 0 and c%2 == 0:
        return (b,c)
    elif b%2 == 0 and d%2 == 0:
        return (b,d)
    elif c%2 == 0 and d%2 == 0:
        return (c,d)
    elif a%2 == 0 and b%2==0 and c%2==0:
        return (a,b,c)
    elif a%2 == 0 and b%2 == 0 and d%2 == 0:
        return (a,b,d)
    elif a%2 == 0 and c%2 == 0 and d%2 == 0:
        return (a,c,d)
    elif b%2 == 0 and c%2 == 0 and d%2 == 0:
        return (b,c,d)
    elif a%2 == 0 and b%2 == 0 and c%2 == 0 and d%2 == 0:
        return (a,b,c,d)
    else:
        return (0)