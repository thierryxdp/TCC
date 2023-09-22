media_matriz(matriz):
    numeros = 0
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            soma = soma + matriz[i][j]
            numeros = numeros + 1
    media = soma/numeros
    return round(2,media)