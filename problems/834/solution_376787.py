def media_matriz(matriz):
   
    contador=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            soma+=matriz[i][j]
            contador +=1
    media = soma/contador
    return round(media,2)