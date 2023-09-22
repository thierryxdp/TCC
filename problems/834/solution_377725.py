def media_matriz(matriz):
    '''recebe uma matriz e cálcula a média de seus números
    list -> float'''
    k = 0
    som = 0
    for lin in matriz:
        for num in lin:
    		som += num
            k += 1
    media = som/k
    return round(media, 2)