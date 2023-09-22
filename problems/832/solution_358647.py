def eh_quadrada(matriz):
    """dada uma matriz, descobre se a matriz é um matriz quadrada (matrizes vazias são quadradas)
    :param matriz: lst(lst, ..., lst)
    :return: bool
    """
    matrizesIguais = 1
    for c in range(len(matriz) - 1):
        if len(matriz[c]) == len(matriz[c + 1]):
            matrizesIguais += 1

    if len(matriz) == 0:
        return True

    elif matrizesIguais == len(matriz) and len(matriz) == len(matriz[0]):
        return True

    else:
        return False