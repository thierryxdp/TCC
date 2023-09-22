def primo(numero):
    i = 2
    while i in range(numero):
        if numero%i != 0:
            i += i
            return False
        else:
            return True