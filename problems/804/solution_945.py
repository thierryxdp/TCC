def filtra_pares(a,b,c,d):
    """filtra apenas os números pares"""
    if a%2 and b%2 and c%2 and d%2:
        return 'erro'
    else:
        return (a,b,c,d)