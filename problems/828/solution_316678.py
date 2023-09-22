def primo(num):
    """
    função que dao um número inteiro positivo, verifica se ele é
    primo ou não de acordo com a quantidade de números que o 
    divide.
    :param n: int
    :return: bool
    """
    primos = 0
    for i in range(1, num + 1):
        if num % i == 0:
            primos += 1

    if primos == 2:
        return True

    else:
        return False