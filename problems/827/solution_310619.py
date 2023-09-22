def qtd_divisores(numero):
    """ - """

    resposta = 0

    for i in range(numero+1):
        if i == 0:
            resposta = resposta 
        elif numero%i == 0:
            resposta += 1

    return resposta