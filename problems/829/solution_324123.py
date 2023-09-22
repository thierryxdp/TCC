def soma_h(numero):
    """ Essa função nos dá o valor do somatório
    harmônico até o valor inserido.

    assinatura: int---> float"""
    soma= 0
    for x in range(numero):
        soma=soma+(1/(x+1))
    return round(soma,2)