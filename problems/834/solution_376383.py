def media_matriz(matriz):
    '''Dada uma matriz de numeros inteiros, calcula e retorna a media de todos os numeros da matriz.
    list -> float'''
    cont = 0

    for i in matriz:
        for j in i:
            cont += j
    media = cont / (len(matriz)*len(matriz[0]))
    return round(media, 2)