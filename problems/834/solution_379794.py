def media_matriz:
    linhas = len(matriz)
    colunas = len(matriz[0])
    float(total) = 0
    for linhas in matriz:
        for colunas in linhas:
            total += float(colunas)
    media = total / float((linhas * colunas))
    
    return round(media,2)