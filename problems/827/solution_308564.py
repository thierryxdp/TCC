def qtd_divisores(num):
    """
    função que recebe umnúmero e retorna a quantidade de
    divisores desse número.
    :param n: int
    :return: int
    """
    divisores = 0
    for i in range(1, num + 1):
        if num % i == 0:
            divisores += 1

    return divisores