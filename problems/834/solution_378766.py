def media_matriz(matriz):
    matrizf=0
    for i in range(len(matriz)):
        linhaf=0
        for j in range(len(matriz[0])):
            linhaf=matriz[i][j]+matriz[i][j]/len(matriz)
        matrizf=linhaf
    return matrizf