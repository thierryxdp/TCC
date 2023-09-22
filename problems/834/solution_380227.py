def media_matriz(matriz):
    '''retorna a media dos elementos da matriz
    list->flout'''
    soma=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
                       soma= soma + matriz[i][j]
    media= soma/(len(matriz)*len(matriz[0]))
    return round(media,2)