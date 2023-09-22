def media_matriz(matriz):
    soma=[]
    linhas= len(matriz)
	colunas= len(matriz[0])
    for i in range(linhas):
        for j in range (colunas):
            soma=matriz[i][j] + soma
            media=soma/(linhas*colunas)
    return media