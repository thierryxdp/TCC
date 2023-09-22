def busca(nome,matriz):
    for i in range(len(matriz)):
        'ola'
        for j in range(len(matriz[0])):
            if nome in matriz[i]:
                del matriz[i][j]
    	return matriz[i][j]