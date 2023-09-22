def media_matriz(matriz):
    """Recebe uma matriz de inteiros e retorna a media de todos os números/list->float"""
    soma=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            soma+=matriz[i][j]
            media=soma/(len(matriz)*len(matriz[0]))
    return round(media,2)