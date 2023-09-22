def insere(lista_numero,n):
	type(lista_numero) == list and type(n) ==int
	lista_ordenada = lista_numero.append(n)
	nova_ordem = lista_numero.sort()
	return nova_ordem