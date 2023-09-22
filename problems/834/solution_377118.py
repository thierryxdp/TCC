def media_matriz(matriz):
    '''Calcula a media de todos os numeros da matriz.
    matriz->float'''
    elementos=len(matriz)
    
    for i in matriz:
        soma=0
        for j in i:
            soma+=j
    media= soma/elementos
    return round(media,2)