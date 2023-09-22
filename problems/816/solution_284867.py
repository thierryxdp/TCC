def maiores(lista_numero,n):
	'Esta função retorna todos os numeros maiores que (n) dentro da lista original'
	'list,int--> list'
	lista = lista_numero[0:] + [n]
	list.sort(lista)
	localisa = list.index(lista, n)
	nova_lista = lista[(localisa+1):]
	return nova_lista