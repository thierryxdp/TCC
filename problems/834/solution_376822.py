def media_matriz(matriz):
    i=1
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            divisor = len(matriz)*len(matriz[0])
            soma=sum(matriz[i])
            media = soma/divisor
    return round(media,2)