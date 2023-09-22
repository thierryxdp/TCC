def media_matriz(matriz):
    media=0
    for linha in matriz:
        for elemento in linha:
            media=media+elemento
        conta= media/(len(matriz)*len(matriz[0]))
    return round(conta,2)