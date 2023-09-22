def media_matriz(matriz):
    media = 0
    soma_n = sum(sum(i) for i in matriz)
    qtd = len(matriz)*len(matriz[0])
    media = soma_n / qtd
    return media