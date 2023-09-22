def media_matriz(matriz):
    soma = 0
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            soma = soma + matriz [i][j]
           media = soma / (len(matriz)*len(matriz[0]))
           return round(media,2)