def maiores(lista, n):
    lista = lista + [n]
    list.sort(lista)
    indice = list.index(lista, n) + list.count(lista, n)
    lista = lista[indice:]
    return lista