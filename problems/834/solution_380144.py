def media_matriz(matriz):
    ''' retorna a media da matriz
    list(list) -> int'''
    som_matriz = 0
    s = 0
    media = som_matriz/s
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            som_matriz += matriz[i][j]
            s += 1
    return media