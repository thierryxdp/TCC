def soma_h(N):
    """
    função que recebe um numero N e retorna o valor de H, que se dá pela
    somatória da sequência apresentada, reduzido para duas casas decimais.
    :param n: int
    :return: float 
    """
    acumulador = 0
    for i in range(1, N + 1):
        H = 1 / i
        acumulador += H

    return round(acumulador, 2)