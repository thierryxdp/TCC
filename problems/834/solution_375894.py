def media_matriz(matriz):
    pos = 0
    soma = 0
    for pos in range(len(matriz)):
        soma += sum(matriz[pos],)/sum(len(matriz[pos]))
    return round(soma,2)