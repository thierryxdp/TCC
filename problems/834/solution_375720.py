def media_matriz(matriz):
    """Pede uma matriz de inteiros não-vazia
    e retorna a média de todos os elementos da matriz
    com precisão de duas casas
    list->float"""
    num_elementos = len(matriz)*len(matriz[0])
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma += matriz[i][j]
    return round((soma/num_elementos),2)