def primo(numero):
    """
    	Recebe um número e diz se ele é primo ou não.
        int --> boolean
    """
    divisor = 2
    while divisor < numero:
        if numero%divisor == 0:
            return False
        divisor += 1

    return True