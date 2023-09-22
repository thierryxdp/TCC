def conta_numero(numero, matriz):
    """Dado um número inteiro e uma matriz de inteiros, conta e retorna quantas vezes o numero aparece na matriz.
    int, list(lists) -> int"""
    x = 0
    y = 0
    for lista in matriz:
        y = y + list.count(matriz[x], numero)
        x = x + 1
    return y