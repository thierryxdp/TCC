def maiores(lista, n):
	list.insert(lista, 0, n)
    list.sort(lista)
    posicao = list.index(lista, n)
    return lista[posicao:]