def media_matriz(matriz):
    """Função que dada como netrada uma matriz de inteiro não vazia, retorna
    a média de todos os números da matriz com duas casas decimais.
    list(list) -> float
    """
    media = 0
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma += matriz[i][j]
            total = len(matriz[0])* len(matriz)
            media = soma/total
    return round(media,2)