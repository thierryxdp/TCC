def filtra_pares(x):
    """retorna uma tupla contendo somente os elemetos pares da tupla original, na mesma ordem que se encontravam.
    tpl->tlp"""
    a,b,c,d=x
    if a%2!=0:
        x=b,c,d
    elif b%2!=0:
        x=a,c,d
    elif c%2!=0:
        x=a,b,d
    elif d%2!=0:
        x=a,b,c
    else:
        return x