def media_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]!=0:
                soma=sum(matriz[i][j])
            return soma