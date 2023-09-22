def filtra_pares(a,b,c,d):
    """filtra apenas os números pares"""
    A = a/2
    B = b/2
    C = c/2
    D = d/2
    if type(A)==float:
        return (b,c,d)
    if type(B)==float:
        return (a,c,d)
    if type(C)==float:
        return (a,b,d)
    if type(D)==float:
        return (a,b,c)