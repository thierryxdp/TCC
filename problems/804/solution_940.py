def filtra_pares(a,b,c,d):
    """filtra apenas os números pares"""
    A = a[-1]%2
    B = b[-1]%2
    C = c[-1]%2
    D = d[-1]%2
    if bool(A)==False:
        return b,c,d