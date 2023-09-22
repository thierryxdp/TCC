def filtra_pares(a,b,c,d):
    """essa funçao retorna uma nova tupla, apenas com os valores pares da tupla original"""
    """entrada: tupla(int, int, int, int)"""
    """saida: tupla(int, int, int, int)"""
    if a%2==0 and b%2==0 and c%2==0 and d%2==0:
        return (a,b,c,d)
    elif a%2==0 and b%2==0 and c%2==0:
        return (a,b,c)
    elif a%2==0 and b%2==0:
        return (a,b)
    elif a%2==0:
        return (a)
    elif a%2==0 and c%2==0:
        return (a,c)
    elif b%2==0 and d%2==0:
        return (b,d)
    else:
        return ()