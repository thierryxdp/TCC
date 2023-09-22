def primo(numero):
    """função que recebe um número inteiro e positivo e verifica se
    o número é primo ou não.
    int -> bool"""
    if numero >= 2:
        for i in range( 2, numero ):
            if not ( numero % i ):
                return False
    else:
        return False

    return True