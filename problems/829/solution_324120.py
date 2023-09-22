def soma_h(numero):
    """ Essa função nos dá o valor do somatório
    harmônico até o valor n.

    assinatura: int---> float"""
    soma= 0
    for x in range(1,numero):
        soma=soma+(1/(x))
    return round(soma,2)