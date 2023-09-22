def media_matriz(matriz):
    '''Dada uma matriz de números inteiros,
    retorna a média de todos os números da
    matriz'''
    soma = 0
    s = matriz.count
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma += matriz[i][j]/s
    return round(soma,2)