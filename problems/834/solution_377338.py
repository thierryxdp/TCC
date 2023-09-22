def media_matriz(matriz):
    """função que recebe uma matriz de inteiros não vazia
    e retorna a media de todos os números da matriz.
    list -> float"""

    total = 0
    soma = 0

    for linha in matriz:
        for aij in linha:
            total += 1
            soma += aij
    media = soma / total

    return round(media, 2)