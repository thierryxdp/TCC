def media_matriz(matriz):
    soma = 0
    for i in matriz:
        soma += sum(i)
    return round((soma/(len(matriz)*len(matriz[0]))),2)