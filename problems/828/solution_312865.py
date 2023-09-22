def primo(numero: int):
    for n in range(2,numero):
        if numero%n==0:
            return False
    else:
        return True