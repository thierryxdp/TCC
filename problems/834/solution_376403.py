def media_matriz(matriz):
    """essa função faz a média dos elementos da matriz de entrada
lista-->float"""
    soma=0
    for x in matriz:
        for v in x:
            soma += v
    elementos = len(matriz[0])*len(matriz)
    media = soma/elementos
    return round(media,2)