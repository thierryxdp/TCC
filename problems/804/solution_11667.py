def filtra_pares (a,b,c,d):
    """retorna uma tupla contendo apenas 
    os elementos pares da tupla original, na mesma
    ordem em que se encontravam"""
    x = (a,b,c,d)
    if a%2 == 0 and b%2 == 0 and c%2 == 0 and d%2 == 0 :
        return a,b,c,d
    elif a%2 == 0 and b%2 == 0 and c%2 == 0 and d%2 == 1:
        return a,b,c
    elif a%2 == 0 and b%2 == 0 and c%2 == 1 and d%2 == 1:
        return a,b
    elif a%2 == 0 and b%2 == 1 and c%2 == 1 and d%2 == 1:
        return a
    elif a%2 == 0 and b%2 == 1 and c%2 == 1 and d%2 == 0:
        return a,d
    elif a%2 == 0 and b%2 == 1 and c%2 == 0 and d%2 == 1:
        return a,c
    elif a%2 == 1 and b%2 == 0 and c%2 == 0 and d%2 == 0:
        return b,c,d
    elif a%2 == 1 and b%2 == 0 and c%2 == 0 and d%2 == 1:
        return b,c
    elif a%2 == 1 and b%2 == 0 and c%2 == 1 and d%2 == 1:
        return b
    elif a%2 == 1 and b%2== 0 and c%2 == 1 and d%2 == 0:
        return b,d
    elif a%2 == 1 and b%2 == 1 and c%2 == 0 and d%2 == 1:
        return c
    elif a%2 == 1 and b%2 == 1 and c%2==0 and d%2==0:
        return c,d
    else:
        return d