def media_matriz(matriz):
    linhas = float(len(matriz))
    colunas = float(len(matriz[0]))
    total = 0
    for linhas in matriz:
        for colunas in linhas:
            total += float(colunas)
    media = total / linhas * colunas
    
    return round(media,2)