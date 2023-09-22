def media_matriz(matriz):
    """calcula a media de todos os elementos;
    list[list[int]]->float"""
    soma=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            soma+=matriz[i][j]
    media=soma/(len(matriz)*len(matriz[0]))
    return round(media,2)