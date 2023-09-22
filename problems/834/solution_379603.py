def media_matriz(matriz):
    ''' retorna a media dos elementos da matriz dada
    list(list) -> float'''
    i=0
    x=0
    for li in range(len(matriz)):
        for co in range(len(matriz[i])):
            x+=matriz[li][co]
        i+=1
    return round(x/(len(matriz)*len(matriz[0])),2)