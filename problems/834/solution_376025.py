def media_matriz(matriz):
    linha=range(len(matriz))
    coluna=range(len(matriz[0]))
    numerador=0
    denominador=len(matriz)
    for i in linha:
            for j in coluna:
                numerador+=matriz[i][j]
    return round(numerador/denominador,2)