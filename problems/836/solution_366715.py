def busca(setor, matriz):
    """ """
    
    for i in range(len(matriz)):
    	if matriz[i][2]== setor:
            list.pop(matriz[i],2)
        elif matriz[i][2] != setor:
            list.pop(matriz[i])
	return matriz