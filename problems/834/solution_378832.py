def media_matriz(matriz):
    """calcula a media de todos os elementos;
    list[list[int]]->float"""
    somal=0
    somat=0
    media=somat/len(matriz)*len(matriz[0])
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            somal+=matriz[i][j]
        somat+=somal
    return media