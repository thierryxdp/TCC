def filtra_pares(a,b,c,d):
    """filtra apenas os números pares em uma lista"""
    tupla = ()
    A = a%2
    B = b%2
    C = c%2
    D = d%2
    if bool(A)==False:
        return (a)
    elif bool (B)==False:
        return (b)
    elif bool (C)==False:
        return (c)
    elif bool (D)==False:
        return (d)
    elif (bool(A) and bool(B))==False:
        return (a,b)