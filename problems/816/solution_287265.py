def maiores(lista,n):
    """
    retorna os elementos de ls que são maiores que n em ordem 
    crescente,  ls(int),int->ls(int)
    """
    if n in lista:
		list.sort(lista)
		lista1 = lista[list.index(lista, n) + 1:]
		return lista1
	else:
		lista.insert(-1, n)
		list.sort(lista)
		lista1 = lista[list.index(lista, n) + 1:]
		return lista1