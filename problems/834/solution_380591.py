def media_matriz(matriz):

    i = 0
    for linha in matriz:
        for elemento in linha:
            i = i + elemento
        media = i/(len(matriz)*len(matriz[0]))
    return round(conta,2)