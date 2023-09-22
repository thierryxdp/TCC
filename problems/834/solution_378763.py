def media_matriz(matriz):
    matrizf=[]
    for i in range(len(matriz)):
        linhaf=[]
        for j in range(len(matriz[0])):
            linhaf.append(matriz[i][j])
        matrizf.append(linhaf)
    return matrizf