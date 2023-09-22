def fatorial(numero):
    ''' funcao que dado o numero retorna o seu fatorial'''
    if numero < 2:
        return 1
    else:
        return numero*fatorial(numero-1