def media_matriz(matriz):
    """Retorna a media dos elementos da matriz dada com entrada;
    list -> float
    """

    soma = 0
    linhas = len(matriz)
    colunas = len(matriz[0])
    elementos = linhas*colunas

    for i in range(linhas):
        for j in range(colunas):
            soma = soma + matriz[i][j]
    media = soma/elementos
    return round(media,2)