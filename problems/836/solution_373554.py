def busca(setor,matriz):
    '''
    '''
    result = []
    for i in range(0,len(matriz)):
    	for j in range(0,len(matriz[0])):
        	if matriz[i][j] == setor:
            	result.append(matriz[i])
    return result