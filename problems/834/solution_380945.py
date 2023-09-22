def media_matriz(matriz):
    """Função que dada uma matriz de inteiros, retorne a média de todos os n°
    da matriz; int => int"""
    x = 0
    for linha in matriz:
        for n in linha:
            x = x + n
        v = x/(len(matriz)*len(matriz[0]))
    return round(v,2)