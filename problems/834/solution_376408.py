def media_matriz(matriz):
    """função que dada uma matriz de inteiros não vazia, retorna a média de todos números de matriz;
    list -> float"""
    acumulador = 0
    divisor = len(matriz)*len(matriz[0])
    for i in range(len(matriz)):
        for c in range(len(matriz[0])):
            acumulador = acumulador + matriz[i][c]
    return round(contador/divisor,2)