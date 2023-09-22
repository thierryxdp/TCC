def maiores(lista, numero):
    """ """
    lista.append(numero)
    lista.sort()
    indice = lista.index(numero)
    return lista[indice + 1:]