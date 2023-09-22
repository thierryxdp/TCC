def filtra_pares(a,b,c,d):
    """filtra apenas os números pares em uma lista"""
    T = (a,b,c,d)
    if (a%2 and b%2 and c%2 and d%2)==0:
        return tuple(T)