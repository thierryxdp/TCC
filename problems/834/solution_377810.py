def media_matriz(matriz):
    '''funcao que calcula a media dos inteiros da matriz;
    list-> int/float'''

    numero=[]
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            list.append(numero,matriz[l][c])
    somatorio = sum(numero)
    mediador=len(numero)
    media= somatorio/mediador
    return round(media,2)