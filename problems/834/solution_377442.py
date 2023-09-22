def media_matriz(matriz):
    linha = len(matriz)
    coluna = len(matriz[0])
    for x in range(linha):
        for y in range(coluna):
            media += matriz[x][y]
            d += 1
    return media / d