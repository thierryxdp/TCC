def primo(numero):
    """ - """

    resposta = 0

    for i in range(numero):
        if i == 0:
            resposta = resposta 
        elif numero%i == 0:
            resposta += 1
    
    if resposta == 1:
        return True
    else:
        return False