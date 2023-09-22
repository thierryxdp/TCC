def faltante(lista):
    """..."""
    y = 0
    list.append(lista, lista[-1] + 1)
    while lista[y+1] == (lista[y] + 2) or None:
        if lista[y+1] == lista[y]+1:
            y = y + 1
        elif lista[y+1] == None:
            y = lista[-1]
    return y