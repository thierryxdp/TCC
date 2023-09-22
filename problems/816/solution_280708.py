def maiores(lista,n):
    """ """
    a = lista + [n]
    b = list.sort(a)
    c = list.index(b,n)
    return a[c:]