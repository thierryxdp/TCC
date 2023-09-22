def media_matriz(matriz):
    soma = 0
    for l in range (len(matriz)):
        soma = soma + sum(matriz[l])
    media = soma / (len(matriz)* len(matriz[0]))
    return round(media,2)