def media_matriz(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    soma = 0
    for i in range(linhas):
        for j in range(colunas):
            soma += matriz[i][j]
    media = soma/(linhas*colunas)
    return round(media, 2)