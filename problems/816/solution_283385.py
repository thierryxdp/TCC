def maiores(lista, n):
    lista = list.append(lista,n)
    list.sort(lista)
    a = list.index(lista, n)
    lista = lista[a:]
    return lista