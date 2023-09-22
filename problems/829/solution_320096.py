def soma_h(n):
    """Funcao calcula e retorna o valor da equacao H = 1 + (1/2) + (1/3) +
    ... + (1/n), aonde n e inteiro e dado na entrada: n """

    h = 0

    for numero in range(1, n+1):
        h += (1/numero)

    return round(h, 2)