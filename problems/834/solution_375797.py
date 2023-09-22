def media_matriz(matriz):
    '''Dada a matriz não vazia de números inteiros, retorna a média de todos os números'''
    '''list->float'''
    soma=0
    for i in range(len(matriz)):
        for i2 in range(len(matriz[0])):
            soma+=matriz[i][i2]
    return round(soma/(len(matriz)*len(matriz[0])),2)