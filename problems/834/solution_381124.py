def media_matriz(matriz):
    m = 0
    for linha in matriz:
        for i in linha:
            m = m + i
        conta = m/(len(matriz)*len(matriz[0]))
    return round(conta,2)