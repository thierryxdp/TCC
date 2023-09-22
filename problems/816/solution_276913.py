def maiores(lista, num):
    """..."""
    L = list.copy(lista)
    list.append(L, num)
    list.sort(L)
    pos = list.index(L, num)
    return L[num+1:]