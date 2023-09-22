def media_matriz(matriz):
    """Dada uma matriz de inteiros não vazia, retorna a média dos
    números da matriz com duas casas decimais de precisão;
    list -> float"""
    soma = 0
    for linha in matriz:
        for e in linha:
            soma+=e
    return round(soma/(len(matriz)*len(matriz[0])), 2)