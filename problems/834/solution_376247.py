def media_matriz(matriz):
    """Função que recebe uma matriz de inteiros não vazia, retornando a media de todos
    os numeros da matriz
    entrada: list(list)
    retorno: float"""
    soma = 0
    for i in range(len(matriz)):
        soma += sum(matriz[i])
    total = len(matriz)*len(matriz[0])
    media = soma / total
    return round(media, 2)