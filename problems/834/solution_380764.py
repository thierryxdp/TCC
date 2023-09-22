media_matriz(matriz):
    for i in matriz:
        for x in matriz[i]:
            x+=x/len(matriz[i])
    return x