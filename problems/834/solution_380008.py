def media_matriz(matriz):
    '''Funcao retorna a media de todos os numeros da matriz,
    com 2 casas decimais; list->float'''
    soma=0
    for i in matriz:
        for j in i:
            soma+=j
    media=(soma/((len(matriz))*len(matriz[0])))
    return round(media,2)