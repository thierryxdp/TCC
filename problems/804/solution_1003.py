def filtra_pares(a,b,c,d):
    """filtra apenas os números pares em uma lista"""
    tupla = ()
    A = a%2
    B = b%2
    C = c%2
    D = d%2
    if (bool(A) and bool(B) and bool(C) and bool(D))==False:
        return (a,b,c,d)