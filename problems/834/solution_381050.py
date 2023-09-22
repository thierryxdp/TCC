def media_matriz(matriz):
    """função que dada uma matriz de inteiros não vazia, retorna a média de todos os números da matriz
    list -> float"""
    from decimal import decimal
    soma = 0
    tamanho = 0
    for linha in matriz:
        soma += sum(linha)
        tamanho += len(linha)
    return decimal(soma / tamanho)