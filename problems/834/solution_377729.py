def media_matriz(matriz):
    '''faz a media dos inteiros da matriz;
    list-> int/float'''

    num=[]
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            list.append(num,matriz[l][c])
    soma = sum(num)
    mediador=len(num)
    media= soma/mediador
    return round(media,2)