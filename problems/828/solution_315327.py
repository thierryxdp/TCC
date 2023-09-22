def primo(numero):
    if numero%2 == 0:
        return False
    for n in range(1, numero+1):
        if n != numero and n%numero != 1 :
            return False
        else:
            return True