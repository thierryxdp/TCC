def media_matriz(matriz):
    """Retorne a média dos números da matriz de entrada"""
    i = 0
    for x in range(len(matriz)):
        for y in range(len(matriz[0])):
            i=i+matriz[x][y]
    media=i/(len(matriz)*len(matriz[0])))
    return (media)