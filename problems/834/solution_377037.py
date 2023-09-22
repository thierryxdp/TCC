def media_matriz (matriz):
    """Recebe uma matriz de inteiros não vazia, e retorna 
    a média de todos os números da matriz, com duas casas de
    precisão.
    list -> int"""
    soma = 0
    elementos = 0
    for linha in matriz:
        for elemento in linha:
            soma += elemento
            elementos += 1
    return round (soma/elementos, 2)