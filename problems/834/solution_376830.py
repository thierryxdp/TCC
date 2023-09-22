def media_matriz(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            divisor = len(matriz)*len(matriz[0])
            soma=soma + matriz[i][j]
            media = soma/divisor
    return round(media,2)