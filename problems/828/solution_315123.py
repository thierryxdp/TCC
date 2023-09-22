def primo(numero):
    for i in range(numero-1,1):
        if numero%i==0:
            return False
    return True