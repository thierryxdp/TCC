def media_matriz:
    linhas = len(matriz)
    colunas = len(matriz[0])
    total = 0
    for linhas in matriz:
        for colunas in linhas:
            total += colunas
    media = total / (linhas * colunas)
    
    return media