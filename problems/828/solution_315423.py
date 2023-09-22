def primo(numero):
    for divisor in range(2, numero):
        if numero%divisor == 0:
            return False
        else:
            return True