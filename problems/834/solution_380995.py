def media_matriz(matriz):
    '''recebendo uma matriz de inteiro nao vazia,
devolve a media dos numeros ali presente. list->int'''
    x = 0
    for z in range(len(matriz)):
        for y in range(len(matriz[z])):
            x=x+m[z][y]
    media=x/(len(matriz)*len(matriz[0]))
    return round(media,2)