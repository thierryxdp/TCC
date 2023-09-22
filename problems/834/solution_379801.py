def media_matriz(matriz):
    linhas = float(len(matriz))
    colunas = float(len(matriz[0]))
    total = 0
    for linha in matriz:
        for coluna in linha:
            total += float(coluna)
            
    media = (linhas * colunas / total) / 10
    
    return round(media,2)