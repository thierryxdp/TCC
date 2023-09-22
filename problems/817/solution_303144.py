def maiores(lista, n):
    if n in lista:
        list.sorte(lista)
        lista1 = lista[list.index(lista, n) +1:]
        return lista1
    else:
        lista.insert(-1, n)
        list.sort(lista)
        lista1 = lista[list.index(lista, n) + 1:]
        return lista1
    media = int(lista) / len(lista)
    return maiores(lista, media)