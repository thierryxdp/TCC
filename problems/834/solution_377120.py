def media_matriz(matriz):
    '''Calcula a media de todos os numeros da matriz.
    matriz->float'''
    elementos=len(matriz)
    elementos1=len(matriz[0])
    total=elementos*elementos1
    soma=0
    for i in matriz:
        for j in i:
            soma+=j
    media= soma/total
    return round(media,2)