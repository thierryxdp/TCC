def filtra_pares(a,b,c,d):
    """filtra apenas os números pares"""
    if a[-1]!=0 or 2 or 4 or 6 or 8:
        return (b,c,d)
    if b[-1]!=0 or 2 or 4 or 6 or 8:
        return (a,c,d)
    if c[-1]!=0 or 2 or 4 or 6 or 8:
        return (a,b,d)
    if d[-1]!=0 or 2 or 4 or 6 or 8:
        return (a,b,c)