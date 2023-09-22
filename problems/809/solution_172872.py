def intercala(lista1, lista2):
	'''Função que recebe duas listas com 3 elementos cada e gera uma nova lista intercalando
	os elementos das duas originais.
	Entrada: lista
	Saída: lista'''
	lista3=lista1[0],lista2[0],lista1[1],lista2[1],lista1[2],lista2[2]
	return list(lista3)