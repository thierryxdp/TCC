def filtra_pares(tupla):
    """..."""
    a = tupla
    b = ()
    if a[0]%2==0:
        b = b + (a[0])
    elif tupla[1]%2==0:
        b = b + (a[1])
    elif a[2]%2 == 0:
        b = b + (a[2])
    elif a[3]%2==0:
        b = b + (a[3])
    else:
        b = ()
    return b