def media_matriz(matriz):
    soma = 0
    coluna = len(matriz[0])
    linha = len(matriz)
    for L in matriz:
        soma1 = 0
        for E in L:
            soma1 = soma1 + E
            soma = soma + soma1
    media = soma/(linha * coluna)
    return round(media,2)