def media_matriz(matriz):
    """calcula a media de todos os elementos;
    list[list[int]]->float"""
    media=0
    somal=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            somal+=matriz[i][j]
        media+=somal
    return media