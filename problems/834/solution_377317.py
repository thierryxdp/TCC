def media_matriz(matriz):
    '''Calcula a média dos numeros de uma matriz com duas casa de
    precisão. list -> float'''
    Media = 0
    Denominador = 0
    for i in matriz:
        for j in i:
            Media = Media + j
            Denominador = Denominador + 1
    return round((Media/Denominador),2)