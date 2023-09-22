def media_matriz(matriz):
    '''calcula a media de todos numeros de uma matriz
    list(list)->float'''
    Media=0
    for i in range(len(matriz)):
        for c in range(len(matriz[0])):
            Media=Media+matriz[i][c]
    return round(Media/(len(matriz)*len(matriz[0])),2)