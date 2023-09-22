def media_matriz(matriz):
    soma=0
    contador=0
    for i in range (len(matriz)):
        for j in range(len(matriz[i])):
            soma +=matriz[i][j]
            contador+=1
    media=soma/contador
    media_formatada={:.2f}.format(media)
    return media_formatada