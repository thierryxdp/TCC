def acima_da_media(lista):
    """..."""
    x = lista
    a = sum(x)
    b = len(x)
    c = a/b
    list.insert(x, 0, c)
    a = sorted(x)
    b = list.index(a, n)
    del a[:b + 1:1]
    return a