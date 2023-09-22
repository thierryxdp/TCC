def maiores(lista, n):
    if n inlista:
        list.sorte(lista)
        lista1 = lista[list.index(lista, n) +1:]
        return lista1
    else:
        lista.insert(-1, n)
        list.sort(lista)
        lista1 = lista[list.index(lista, n) +:]
        return lista1