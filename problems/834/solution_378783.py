def media_matriz(matriz):
    matrizf = []
    
    for i in range(len(matriz)):
        linhaf = []
        for j in range(len(matriz[0])):
            linhaf.append(matriz[i][j]/2)
        matrizf.append(linhaf)
    return matrizf