def maiores(lista, n):
    """..."""
    x = lista
    a = sorted(x)
    b = list.index(a, n)
    del a[:b:]