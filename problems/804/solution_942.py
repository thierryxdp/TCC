def filtra_pares(a,b,c,d):
    """filtra apenas os números pares"""
    A = a/2
    B = b/2
    C = c/2
    D = d/2
    if bool(A)==False:
        return (b,c,d)
    if bool(B)==False:
        return (a,c,d)
    if bool(C)==False:
        return (a,b,d)
    if bool(D)==False:
        return (a,b,c)