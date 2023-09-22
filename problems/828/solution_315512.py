def primo(numero):
    for x in range(2, numero):
        if numero % x == 0:
            return True
    return False