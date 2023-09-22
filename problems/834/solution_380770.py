def media_matriz(matriz):
    soma=0
    for i in range(len(matriz)):
        for x in matriz[i]:
            soma=soma+x
            soma/len(matriz[i])
    return round(x,2)