def busca(setor, matriz_de_funcionarios):
	'''Função que recebe uma palavra indicando o setor do qual se quer encontrar e uma matriz de quatro entradas onde o seu numero de linhas depende do numero de funcionarios, e retorna uma lista contendo as informações dos funcionarios que trabalham naquele setor'''
	''' str, list -> list '''
	lista_de_procura = []
	i = 0
	while i < len(matriz):
		if setor in matriz_de_funcionarios[i]:
			list.append(lista_de_procura, matriz[i])
		i += 1
	return lista_de_procura