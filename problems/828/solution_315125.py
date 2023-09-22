def primo(numero):
    for i in range(2,numero-1):
        if numero%i==0:
            return False
    return True