def media_matriz(matriz):
    '''Calcula a media de todos os numeros da matriz.
    matriz->float'''
    soma=sum(matriz)
    elementos=len(matriz)
    media= soma/elementos
    return round(media,2)