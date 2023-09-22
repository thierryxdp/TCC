def media_matriz (matriz):
    '''c'''
    vari=0
    for i in range(len(matriz)):
        for j in i:
            vari+= matriz[i][j]
    return vari/j