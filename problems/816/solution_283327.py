def maiores(lista, n):
    """..."""
    x = lista
    list.insert(x, 0, n)
    a = sorted(x)
    b = list.index(a, n)
    del a[:b:1]