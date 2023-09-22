def faltante(lista):
    """..."""
    y = 0
    list.append(lista, lista[-1] + 1)
    while lista[y] == y + 1:
        if lista[y] in lista[0:-2]:
            y = y + 1
        elif lista[y] == lista[-1]:
            y = lista[-2]
    return y + 1