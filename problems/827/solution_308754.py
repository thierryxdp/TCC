def qtd_divisores(numero):
    """
    função que recebe um numero e retorna a quantidade de divisores que ele possui
    int---> int
    """
    divisores = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores += 1

    return divisores