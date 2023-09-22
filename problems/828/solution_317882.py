def primo(numero):
    """Funcao que diz se o numero é primo.
    int->bool"""
    for count in range(2,numero):
        if (numeros % count == 0):
            return False
        else:
            return True