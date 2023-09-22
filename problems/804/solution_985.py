def filtra_pares(a,b,c,d):
    """filtra apenas os números pares em uma lista"""
    A = a%2
    B = b%2
    C = c%2
    D = d%2
    if (bool(A)==False) and (bool(B)==False) and (bool(C)==False) and (bool(D)==False):
        return (a,b,c,d)
    if (bool(A)==False) and (bool(B)==False) and (bool(C)==False) and (bool(D)==True):
        return (a,b,c)
    if (bool(A)==False) and (bool(B)==False) and (bool(C)==True) and (bool(D)==False):
        return (a,b,d)
    if (bool(A)==False) and (bool(B)==True) and (bool(C)==False) and (bool(D)==False):
        return (a,c,d)
    if (bool(A)==True) and (bool(B)==False) and (bool(C)==False) and (bool(D)==False):
        return (b,c,d)