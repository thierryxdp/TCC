def media_matriz(matriz):
    if matriz!=[]:
        soma=0
        for linha in matriz:
            soma+=sum(linha)
    	return soma/(len(matriz)*len(matriz[1]))