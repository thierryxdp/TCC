def media_matriz(matriz):
    """A função recebe uma entrada uma matriz de inteiros não vazia e
    retorna a media dos numeros;
    list(list) -> float"""
    soma = 0
    divisao = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            soma += matriz[i][j]
            divisao += 1
    media = soma/divisao
    return round(media,2)