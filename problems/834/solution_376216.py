def media_matriz(matriz):
    somatorio=0
    resultado=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            somatorio=somatorio+matriz[i][j]
            resultado= somatorio/j
    return somatorio