def filtra_pares(a,b,c,d):
    """filtra apenas os números pares"""
    if a%2:
        return (b,c,d)
    else:
        return (a,b,c,d)