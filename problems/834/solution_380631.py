def media_matriz(matriz):
    soma=0
    linhas= len(matriz)
	colunas= len(matriz[0])
    for i in range(linhas):
        for j in range (colunas):
            soma=matriz[i][j] + soma
            media=soma/(linhas*colunas)
    return media[0:2]