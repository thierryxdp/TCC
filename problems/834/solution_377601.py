def media_matriz(matriz):
    soma=0
    
    for i in range(len(matriz)):
        for k in range(len(matriz[0])):
           soma+=matriz[i][k]
           
    media =soma/len(matriz)
    return media