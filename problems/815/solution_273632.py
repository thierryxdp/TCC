def insere(lista_numero,n):
	'Esta função coloca a lista em ordem crescente de forma que continue ordenada'
	'list,int--> list'
	lista = lista_numero[0:] + [n]
	list.sort(lista)
	return lista