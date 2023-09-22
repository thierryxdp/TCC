def maiores(lista, n):
    """..."""

    if n in lista:
        list.sort(lista)
        x = list.index(lista, n)
        nova_lista = lista[x:]

        return nova_lista

    if n not in lista:
        list.append(lista, n)
        list.sort(lista)
        x = list.index(lista, n)
        nova_lista = lista[x:]

        return nova_lista