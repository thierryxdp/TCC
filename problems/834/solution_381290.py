def media_matriz(matriz):
    soma=0
    for linha in matriz:
        soma+=sum(linha)
    media=soma/(len(matriz[1])*len(matriz))
    return round(media,2)