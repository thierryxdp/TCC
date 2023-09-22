def busca(setor, matriz_de_funcionarios):
    '''Função que recebe uma palavra indicando o setor do qual se quer encontrar e uma matriz de quatro entradas onde o seu numero de linhas depende do numero de funcionarios, e retorna uma lista contendo as informações dos funcionarios que trabalham naquele setor'''
	''' str, list -> list '''
	lista_de_funcionarios = []
	for elementos in matriz_de_funcionarios:
		if setor in elementos:
			list.remove(elementos, setor)
			list.append(lista_de_funcionarios, elementos)
	return lista_de_funcionarios