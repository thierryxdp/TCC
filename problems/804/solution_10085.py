def filtra_pares(a,b,c,d):
    """essa funçao retorna uma nova tupla, apenas com os valores pares da tupla original"""
    """entrada: tupla(int, int, int, int)"""
    """saida: tupla(int, int, int, int)"""
    if a%2==0, b%2==0, c%2==0 and d%2==0:
        return (a,b,c,d)
    elif a%2=!0, b%2==0, c%2==0 and d%2==0:
        return (b,c,d)
    elif a%2=!0, b%2=!0, c%2==0 and d%2==0:
        return (c,d)
    elif a%2=!0, b%2=!0, c%2=!0 and d%2==0:
        return (d)
    else:
        return ()