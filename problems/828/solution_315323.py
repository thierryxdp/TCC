def primo(numero):
    for n in range(1, numero+1):
        if n%2 == 0:
            return False
        if numero%n != 0:
            return True