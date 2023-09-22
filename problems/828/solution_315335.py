def primo(numero):
    if numero%2 == 0:
        return False
    for n in range(1, numero+1):
        if numero%n != 0 and numero/n == numero :
            return True
        else:
            return False