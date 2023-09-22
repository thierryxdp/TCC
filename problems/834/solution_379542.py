def media_matriz(matriz):
    """Dada uma matriz de inteiros, retorna a média de todos os numeros da matriz.
    list(lists) -> float"""
    x = 0
    for i in matriz:
        for j in i:
            x = x + j
    y = len(matriz)*len(matriz[0])    
    return round(x/y, 2)