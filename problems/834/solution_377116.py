def media_matriz(matriz):
    '''Calcula a media de todos os numeros da matriz.
    matriz->float'''
    elementos=len(matriz)
    soma=0
    for i in matriz:
        for j inn i:
            soma+=j
    media= soma/elementos
    return round(media,2)