def media_matriz(matriz):
    quantidade=0
    soma=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            soma=soma+matriz[i][j]
    quantidade=quantidade+1
    return round(soma/quantidade,2)