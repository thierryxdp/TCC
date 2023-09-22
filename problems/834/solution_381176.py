def media_matriz(matriz):
    cont = 0
    somatorio = []
    comprimento = []
    for linha in matriz:
        for aij in linha:
            somatorio = sum(linha)
            comprimento = len(linha)
            media = (somatorio/comprimento)
    return round(media,2)