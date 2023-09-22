def busca(setor, matriz):
	'''Recebe uma matriz com nome, registro,
    setor e telefone de um funcionario todos
    em str, e recebe tambem um dos setores
    informados, retorna os dados de todos os
	funcionarios de determinado setor
	
    str -> list
    '''
	dados = []
	for i in range(len(matriz)):
		if setor in matriz[i]:
			dados.append(matriz[i])
	for j in range(len(dados)):
		if dados[j][2] == setor:
			del dados[j][2]