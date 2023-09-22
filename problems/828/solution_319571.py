def primo(numero):
    i = 2
    for i in range(numero):
        if numero%i != 0:
            i += i
            return False
        else:
            return True