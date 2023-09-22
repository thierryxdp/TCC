def qtd_divisores(numero):
    """ - """

    resposta = 0

    for i in range(numero):
        if numero%i == 0:
        resposta += 1

    return resposta