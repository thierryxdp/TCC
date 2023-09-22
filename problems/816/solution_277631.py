def maiores(lista, n):
    listacopia = lista[::]
    lista0 = list.insert(lista, 0, n)
    lista1 = list.sort(lista)
    antesdn = lista[:n]
    return list.remove(lista, antesdn)