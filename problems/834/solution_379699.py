def media_matriz(matriz):
    '''
    dada uma matriz de números inteiros não vazia, retorna a média
    de todos os seus elementos. O valor retornado deve possuir duas casas
    decimais de precisão

    array -> float
    '''

    soma = 0
    z = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma = soma + matriz[i][j]
            z = z + 1
            
    media = round(soma/z, 2)
    return media