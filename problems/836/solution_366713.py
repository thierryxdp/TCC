def busca(setor, matriz):
    """ """
    
    for i in matriz:
    	if matriz[i][2]== setor:
            list.pop(matriz[i],2)
        else:
            list.pop(matriz[i])
	return matriz