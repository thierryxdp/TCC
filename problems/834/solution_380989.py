def media_matriz(matriz):
    '''Função que retorna a média de todos os números
    da matriz, dada uma matriz de inteiros não vazia; list->int'''
    x = 0
    for i in range(len(matriz)):
        for y in range(len(matriz[i])):
            x=x+matriz[i][y]
    media=x/(len(matriz)*len(matriz[0]))
    return round(media,2)