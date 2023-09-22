def primo(numero):
    for i in range(1,numero):
        if numero%i==0:
            return False
    return True