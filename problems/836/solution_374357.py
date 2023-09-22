def busca(informacao,matriz):
    ''' '''
    for linha in range(len(matriz)):
    	for coluna in range(len(matriz[linha])):
            if informacao == matriz[linha][coluna]:
            	return matriz[linha]