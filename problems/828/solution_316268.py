def primo(numero):
    for divisores in range(2,numero):
        if numero%divisores == 0:
            return False
        else:
            return True