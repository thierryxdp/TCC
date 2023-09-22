def intercala(lista1, lista2):
	"""Função que gera um lista intercalando os elementos da lista 1 e lista 2
    list->list"""
	lista3=list()
	lista3.append(lista1[0])
	lista3.append(lista2[0])
	lista3.append(lista1[1])
	lista3.append(lista2[1])
	lista3.append(lista1[2])
	lista3.append(lista2[2])
	return lista3