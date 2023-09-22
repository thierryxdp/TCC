def media_matriz(matriz):
    matrizf=0
    for i in range(len(matriz)):
        linhaf=[]
        for j in range(len(matriz[0])):
            linhaf.append(matriz[i][j]+matriz[i][j])
        matrizf.append(linhaf)
    return matrizf