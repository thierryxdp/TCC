def maiores(lista, n):
    list = lista
    list.append(n)
    list.sort()
    lista = lista[(list.index(lista, n)):]
    return lista