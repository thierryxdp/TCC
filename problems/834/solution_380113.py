def media_matriz(matriz):
    '''Funçao que retorna a media dos números
    de uma matriz'''
    'list ----> float'
    n=len(matriz)
    for i in matriz:
        if matriz != 0:
            mm=sum(matriz%n)
    return mm