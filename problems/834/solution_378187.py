def media_matriz(matriz):
    soma = 0
    n = 0
    for i in range(len(matriz)):
        for j in matriz[i]:
            soma = soma + j
            n = n + 1
    media = soma/n
    return round(media, 2)