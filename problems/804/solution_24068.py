def filtra_pares(a,b,c,d):
    '''Função que recebe uma tupla e retorna a mesma tupla
    com somente elementos pares; tupla->tupla'''
    if a%2==0:
        return (a,)
    elif a%2==0 and b%2==0:
        return (a,b)
    elif a%2==0 and b%2==0 and c%2==0:
        return (a,b,c)
    elif a%2==0 and b%2==0 and c%2==0 and d%2==0:
        return (a,b,c,d)
    elif b%2==0:
        return (b,)
    elif b%2==0 and c%2==0:
        return (b,c)
    elif b%2==0 and c %2==0 and d%2==0:
        return(b,c,d)
    elif c%2==0:
        return (c,)
    elif c%2==0 and d%2==0:
        return (c,d)
    elif d%2==0:
        return (d,)