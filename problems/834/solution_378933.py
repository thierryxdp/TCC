def media_matriz(matriz):
    '''função que retorna a média de todos os números da matriz'''
    '''list(list)->float'''
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            soma = soma + matriz[i][j]
    n = len(matriz)*len(matriz[0])
    media = soma/n
    return round(media,2)