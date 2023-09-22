def media_matriz(matriz):
    for l in range(len(matriz)):
        for i in range(len(matriz[0])):
            matriz=sum(matriz[l])
            matriz=matriz/(len(matriz[0]))
        return matriz