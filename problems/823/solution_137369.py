def faltante(lista):
	'''esta função recebe lista e retorna elementos que falta
	list --> int'''
	list.sort(lista)
	lista_ordenada = list(range(1, len(lista)+2))
	ctd = 0
	while len(lista_ordenada) > ctd+1:
		if lista[ctd] != lista_ordenada[ctd]:
			return lista_ordenada[ctd]
		ctd +=1
	return lista_ordenada[-1]