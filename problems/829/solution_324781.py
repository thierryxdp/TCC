def soma_h(numero):
    """ Função que irá calcular e retornar o valor de H com N termos. Int > float """

    resposta = 0

    for i in range(numero+1):
        if i == 0:
            resposta = resposta
        else:
            resposta = resposta + 1/i

    resposta = round(resposta,2)
    return resposta