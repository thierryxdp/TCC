def filtra_pares(tp):
    """Funcao que recebe uma tupla com quatro elementos inteiros como
parametro, e retorna uma nova tupla contendo apenas os elementos pares
da tupla original, na mesma ordem em que se encontravam; 
tuple -> tuple"""
    a,b,c,d = tp
    if a%2 == 0 and b%2 == 0 and c%2 == 0 and d%2 == 0:
        return a,b,c,d
    elif b%2 == 0 and c%2 == 0 and d%2 == 0:
        return b,c,d
    elif a%2 == 0 and c%2 == 0 and d%2 == 0:
        return a,c,d
    elif a%2 == 0 and b%2 == 0 and d%2 == 0:
        return a,b,d
    elif a%2 == 0 and b%2 == 0 and c%2 == 0:
        return a,b,c
    elif c%2 == 0 and d%2 == 0:
        return c,d
    elif b%2 == 0 and d%2 == 0:
        return b,d
    elif b%2 == 0 and c%2 == 0:
        return b,c
    elif a%2 == 0 and d%2 == 0:
        return a,d
    elif a%2 == 0 and c%2 == 0:
        return a,c
    elif a%2 == 0 and b%2 == 0:
        return a,b
    elif d%2 == 0:
        return d,
    elif c%2 == 0:
        return c,
    elif b%2 == 0:
        return b,
    elif d%2 == 0:
        return d,
    else:
        return ()