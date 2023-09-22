def media_matriz(matriz):
    '''Calcula a media dos valores da matriz, arredondando para duas casas decimais
    list -> float'''
    total = 0
    for x in matriz:
        for y in range(len(x)):
            total += x[y]
    media = total / (len(x) * len(matriz))
    return round(media,2)