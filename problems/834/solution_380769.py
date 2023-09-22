def media_matriz(matriz):
    for i in range(len(matriz)):
        for x in matriz[i]:
            x+=x/len(matriz[i])
    return round(x,2)