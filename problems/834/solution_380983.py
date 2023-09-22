def media_matriz(matriz):
    '''funçao que dada uma matriz de inteiros não vazia, retorna a média de todos os números
    da matriz; list->int'''
    m = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            m=m+matriz[i][j]
    media=m/(len(matriz)*len(matriz[0]))
    return round(media,2)