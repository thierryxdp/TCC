def soma_h(x):
    """ Calcula e retorna o valor de H com N, e retorna seu resultado
    somente com 2 casas decimais.
    assinatura: int --> float
    """
    soma= 0
    for i in range (1, x +1):
        soma= soma + 1/i
    return round(soma, 2)