def soma_h(numero):
    """ - """

    resposta = 0
    contador = 0

    while contador < numero+1:
        if contador == 0:
            resposta = resposta
        else:
            resposta = resposta + 1/contador
        contador = contador+1
 
    resposta = round(resposta,2)
    return resposta