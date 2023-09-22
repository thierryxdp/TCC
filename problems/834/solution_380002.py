def media_matriz(matriz):
    ''' '''
    soma=0
    for i in matriz:
        for j in i:
            soma+=j
        media=(soma/len(matriz[0]))
    return round(media)