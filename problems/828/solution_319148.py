def primo(numero):
    """ - """

    resposta = 0
    contador = 0

    while contador < numero:
        if contador == 0:
            resposta = resposta
        elif numero%contador == 0:
            resposta += 1
        contador = contador +1     

    if resposta == 1:
        return True
    else:
        return False