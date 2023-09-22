def media_matriz(matriz):
    soma=0
    for linha in matriz:
        for i in linha:
            soma+=i
    return round(soma/(len(matriz)*len(matriz[0])),2)