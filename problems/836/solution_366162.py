def busca(setor, matriz):
	'''Dado uma string setor e uma matriz, retorna uma 
    lista com os funcionarios pertencentes ao setor e 
    suas informações
    	str, list -> list'''
	funcionarios = []
	for i in matriz:
		if i[2] == setor:
			funcionarios += [[i[0],i[1],i[3]]]
	return funcionarios