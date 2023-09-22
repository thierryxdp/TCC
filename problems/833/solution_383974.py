def conta_numero(numero, matriz):
    """dado um número inteiro conta quantas vezes esse número está na matriz
    :param numero: int or float or complex
    :param matriz: lst(lst, ..., lst)
    :return: int
    """
    vezes = 0
    for c in range(len(matriz)):
        for i in range(len(matriz[c])):
            if numero == matriz[c][i]:
                vezes += 1
    return vezes