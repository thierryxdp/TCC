def media_matriz(matriz):
    """Recebe uma matriz de inteiros não vazia, e retorna a média de todos seus
    termos com duas casas decimais de precisão
    list -> float"""
    soma_termos = 0
    num_termos = len(matriz)*len(matriz[0])
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            soma_termos += matriz[i][j]
    media = soma_termos/num_termos
    return round(media, 2)