def media_matriz(matriz):
    '''Esta função retorna a média de todos os números de uma matriz de inteiros não vazia, com duas casas decimais de precisão.
list->float'''
    soma=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma=soma+matriz[i][j]
    total=len(matriz)*len(matriz[0])
    media=soma/total
    return round(media,2)