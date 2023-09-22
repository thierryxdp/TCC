def media_matriz(matriz):
    soma=0
    contador=0
    for i in range (len(matriz)):
        for j in range(len(matriz[i])):
            soma +=matriz[i][j]
            contador+=1
    media=soma/contador
    return float("{.2f}"format(media))