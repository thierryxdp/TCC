def media_matriz(matriz):
    """dada uma matriz de inteiro não vazia retorna a média com 2 casas decimais de aproximação de todos os números
    :param matriz: lst(lst, ..., lst)
    :return: float or int
    """
    soma = divisor = 0
    for c in range(len(matriz)):
        for i in range(len(matriz[c])):
            soma += matriz[c][i]
            divisor += 1

    return round(soma/divisor, 2)