def faltante(lista):
	'''funcao onde recebe lista e retorna elemento que falta list--> int'''
	list.sort(lista)
	lista_ordenada = list(range(1, len(lista)+2))
	contador = 0
	while len(lista_ordenada) > contador+1:
		if lista[contador] != lista_ordenada[contador]:
			return lista_ordenada[contador]
		contador +=1
	return lista_ordenada[-1]