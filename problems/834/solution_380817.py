def media_matriz(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    soma = 0
    for i in range(linhas):
        for j in range(colunas):
            soma = soma + matriz[i][j]
    media = soma / (linhas * colunas)
    media = round(media,2)
    return media