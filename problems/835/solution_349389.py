def melhor_volta(matriz_da_corrida):
    '''Função que recebe de entrada uma matriz de tamanho 6 x 10, onde 6 linhas indica o numero de corredores, as 10 colunas o numero de voltas, e cada elemento representa o tempo de cada volta, e retorna uma tupla contendo qual corredor for melhor na prova, em qual tempo e em qual volta'''
	''' list -> tuple'''
	linha = 0
	corredor = 0
	volta = 0
	minimo = []
	for i in matriz_da_corrida:
		list.append(minimo, min(i))
		list.sort(minimo)
	tempo = minimo[0]
	for i in matriz_da_corrida:
		if minimo [0] in i:
			corredor = linha + 1
			volta = list.index(i, minimo[0]) +1
		linha += 1
	return corredor, tempo, volta