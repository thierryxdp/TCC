def filtra_pares(tupla):
    """..."""
    a = tupla
    b = ()
    c = ()
    d = ()
    e = ()
    if a[0]%2==0:
        b = (a[0],)
    elif tupla[1]%2==0:
        c = (a[1],)
    elif a[2]%2 == 0:
        d = (a[2],)
    elif a[3]%2==0:
        e = (a[3],)
    return b + c + d + e