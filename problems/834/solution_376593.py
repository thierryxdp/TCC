def media_matriz(matriz):
    soma=0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            soma=soma+(matriz[i][j])
    return soma