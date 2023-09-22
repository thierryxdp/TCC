import numpy as np
def media_matriz(matriz):
    """Função que dada uma matriz de inteiros não vazia,
    retorna a média de todos os números da matriz (com
    exatamente duas casas decimais de precisão);
    list, list-> float"""
    a = np.array(matriz)
    final = np.mean(a)
    return round(final, 2