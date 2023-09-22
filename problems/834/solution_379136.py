def media_matriz(matriz):
    """Dada uma matriz de inteiros não vazia, retorna a média
    de todos os números da matriz (com exatamente duas casas
    decimais de precisão);
    list -> float"""
    soma = 0
    quantidade = 0
    for linha in matriz:
        for aij in linha:
            soma += aij
            quantidade += 1
    return round((soma/quantidade), 2)