def media_matriz(matriz):
    acumulador=0
    contador=0
    linha=len(matriz)
    coluna=len(matriz[0])
    for i in range(linha):
        for j in range(coluna):
            acumulador=acumulador+matriz[i][j]
            contador=contador+1
        return round(acumulador/contador,2)