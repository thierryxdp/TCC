def media_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            divisor = len(matriz)*len(matriz[0])
            soma=sum(matriz[i])+sum(matriz)
            media = soma/divisor
    return round(media,2)