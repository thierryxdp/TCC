def acima_da_media(lista):
    """..."""
    x = lista
    a = sum(x)
    b = len(x)
    c = a/b
    list.insert(x, -1, c)
    a = sorted(x)
    b = list.index(a, c)
    del a[:b + 1:1]
    del a[b]
    return a