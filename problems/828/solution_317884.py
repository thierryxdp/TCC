def primo(numero):
    """Funcao que diz se o numero é primo.
    int->bool"""
    for count in range(2,numero+1):
        if (numero % count == 0):
            return False
        else:
            return True