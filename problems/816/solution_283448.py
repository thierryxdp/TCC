def maiores(lista, n):
    """Dada uma lista de números e um número n, gera uma nova lista contendo os números maiores do que n
    e os inserem dentro dessa nova lista.
	int-->int"""
    list(lista)
    lista.append(n)
    listsorted = sorted(lista)
    listaindex = listasorted.index(n)
    if n not in listasorted:
        lista.append(n)
    return listasorted[listaindex + 1:]