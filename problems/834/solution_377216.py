def media_matriz(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += sum(matriz[i])
    return round((soma/(len(matriz)*len(matriz[0]))),2)