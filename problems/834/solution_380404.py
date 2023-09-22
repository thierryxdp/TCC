def media_matriz(matriz):
    """ Esta função calcula a média entre as matrizes
    dict -> float """
    soma = 0
    tamanho = 0

    for linha in matriz:
        soma += sum(linha)
        tamanho += len(linha)

    return soma / tamanho