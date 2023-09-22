def media_matriz(matriz):
    Nelementos=len(matriz)*len(matriz[0])
    somatotal=0
    for i in range(len(matriz)):
        soma=0
        for j in range(len(matriz[0])):
            soma+=matriz[i][j]
        somatotal+=soma
    return somatotal/Nelementos