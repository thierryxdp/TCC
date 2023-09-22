def media_matriz(matriz):
    """
    Essa função recebe uma matriz e retorna a média de todos os termos 
    da matriz;
    list -> float
    """
    soma = 0
    for i in matriz:
        for j in i:
            soma += j
    n_termos = len(matriz[0]) * len(matriz)
    media = soma / n_termos
    return round(media, 2)