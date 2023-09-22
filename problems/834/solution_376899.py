def media_matriz(matriz):
    lista=[]
    soma=0
    contador=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma+=matriz[i][j]
            contador+=1
    media= soma/contador
    return round(soma,2)