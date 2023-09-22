def maiores(lista, n):
    if n not in lista:
        list.sort(lista)
        return lista
    else:
        list.sort(lista)
        del lista[:n]
        return lista