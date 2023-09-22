def filtra_pares(tupla):
    """Dada uma tupla, filtra os pares e retorna uma tupla com apenas os pares da tupla original, na mesma ordem
    tupla -> tupla"""
    a = tupla
    b = ()
    c = ()
    d = ()
    e = ()
    if a[0]%2==0:
        b = (a[0],)
    if a[1]%2==0:
        c = (a[1],)
    if a[2]%2 == 0:
        d = (a[2],)
    if a[3]%2==0:
        e = (a[3],)
    return b + c + d + e