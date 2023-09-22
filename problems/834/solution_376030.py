def media_matriz(matriz):
    """ faz a media aritmetica de matrizes quadradas"""
    linha=range(len(matriz))
    coluna=range(len(matriz[0]))
    numerador=0
    denominador=len(matriz)*len(matriz[0])
    for i in linha:
            for j in coluna:
                numerador+=matriz[i][j]
    return round(numerador/denominador,2)