def primo(numero):
    for n in len(numero+1):
        if numero%n == 0 and numero%2 == 0:
            return True
        else: return False