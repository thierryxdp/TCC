def media_matriz(matriz):
    """Dada uma matriz de inteiros não vazia
    retorna uma média de todos os números da matriz."""
    soma = 0
    tamanho = 0
    for linha in matriz:
        soma += sum(linha)
        tamanho += len(linha)
    return round(soma/tamanho,2)