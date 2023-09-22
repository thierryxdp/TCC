def maiores(lista,n):
    """ """
    a = lista + [n]
    list.sort(a)
    c = list.index(a,n)
    return a[c+1:]