def busca(setor,matriz):
    '''
    '''
    result = []
    for i in range(0,len(matriz)):
        linha = []
    	for j in range(0,len(matriz[0])):
        	if matriz[i][j] == setor:
            	linha.append(matriz[i])
                del(linha[j])
                result.append(linha)
    return result