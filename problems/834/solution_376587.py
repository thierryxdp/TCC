def media_matriz(matriz):
    soma = 0
    for linhas in matriz:
        for colunas in linhas:
            soma = colunas + soma
    media = soma / (len(matriz)*len(matriz[0]))
    return round(media,2)