def busca(setor, matriz):
    """ """
    resultado = []
    for i in range(len(matriz)):
    	if matriz[i][2]== setor:
            list.pop(matriz[i],2)
            resultado.append(matriz[i])
	return matriz