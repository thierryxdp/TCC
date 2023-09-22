def media_matriz(matriz):
    """Função que, dado uma matriz de números inteiros, retorna a média de todos os números da matriz.
    list -> float"""
    soma = 0
    soma1 = map(lambda x: x[0]+soma, matriz)
    return soma1/(len(matriz)*len(matriz[0]))