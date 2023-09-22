def media_matriz(matriz):
    '''retorna a media dos números da matriz'''
    div=len(matriz)*len(matriz[0])
    aux=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            aux=aux+matriz[i][j]
    return round(aux/div,2)