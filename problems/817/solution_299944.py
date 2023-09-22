def maiores(lista_numero,n):
	
	'list,int--> int
	lista = lista_numero[0:] + [n]
	list.sort(lista)
	x = list.index(lista, n)
	nova_lista = lista[(x+1):]
	lis = sum(nova_lista)
	media_lista = lis/len(nova_lista)
	return media_lista