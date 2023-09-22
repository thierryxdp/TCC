def insere(lista_numero,n):
    """Função que insere um número n em uma lista, e, depois, a ordene, com esse número n já inserido, de forma correta.
    list,float=>list"""
	list.insert(lista_numero, 0, n)
	list.sort(lista_numero)
	return lista_numero