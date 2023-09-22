def media_matriz(matriz):
    l=len(matriz)
    c=len(matriz[0])
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma = soma + matriz[i][j]
            media = soma/(l*c)
    return round(media,2)