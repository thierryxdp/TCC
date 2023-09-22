def media_matriz(matriz):
    media = 0
    d = 0
    linha = len(matriz)
    coluna = len(matriz[0])
    for x in range(linha):
        for y in range(coluna):
            media += matriz[x][y]
            d += 1
    return media / d