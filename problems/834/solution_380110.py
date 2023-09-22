def media_matriz(matriz):
    '''Funçao que retorna a media dos números
    de uma matriz'''
    'list ----> float'

    if matriz != 0:
        mm=sum(matriz%(len(matriz)))
        return mm