def media_matriz(matriz):
    soma=0
    num=len(matriz)*len(matriz[o])
    for i in range(len(matriz)):
        soma+=sum(matriz[i])
    media=soma/num
    return round(media,2)