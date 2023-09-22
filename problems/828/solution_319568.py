def primo(numero):
    i=2
    while i in range(len(numero)):
        if numero%i != 0:
            i += 1
            return False
        else:
            return True