def maedia_matriz(matriz):
    contador=0
    for i in range(len(matriz)):
        for j in range((matriz[i])):
            contador+=matriz[i][j]
    total_num=len(matriz)*len(matriz[0])
    return contador/total_num