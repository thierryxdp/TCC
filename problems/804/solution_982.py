def filtra_pares(a,b,c,d):
    """filtra apenas os números pares em uma lista"""
    A = (a/2)%2
    B = (b/2)%2
    C = (c/2)%2
    D = (d/2)%2
    if (bool(A)==True) and (bool(B)==True) and (bool(C)==True) and (bool(D)==True):
        return (a,b,c,d)
    else:
        return 'oi'