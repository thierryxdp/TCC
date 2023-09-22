def faltante(lista):
	''' Esta função recebe uma lista e retorna 0 elemento que
    faltava
	list -> int'''
   
	list.sort(lista)
	lista_ordenada = list(range(1, len(lista)+2))
	contador = 0