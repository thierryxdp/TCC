def media_matriz(matriz):
    """funcao que calcula a media de todos elementos de uma matriz;
    list->float"""
    soma=0
    elementos=len(matriz)*len(matriz[0])
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            soma=soma+matriz[i][j]
    media=soma/elementos
    return round(media,2)