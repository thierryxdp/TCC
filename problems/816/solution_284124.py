def maiores(lista, n):
    lista = lista + [n]
    list.sort(lista)
    if n < lista[1]:
        return lista[1:]