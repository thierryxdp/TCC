def primo(numero):
    for n in range(1, numero+1):
        if numero%n == 0 and numero%2 == 0:
            return True
        else: return False