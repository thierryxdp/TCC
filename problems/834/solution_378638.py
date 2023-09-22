def media_matriz(matriz):
    '''retorna a média de todos os numeros da matriz; list->float'''
    soma=0
    lin=len(matriz)
    col=len(matriz[0])
    elementos=lin*col
    for i in matriz:
        for j in i:
            soma+=j
    media=(soma/elementos)
    
    return round(media,2)