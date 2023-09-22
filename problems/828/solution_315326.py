def primo(numero):
    for n in range(1, numero+1):
        if n%2 == 0:
            return False
        if n != numero and n%numero != 1 :
            return False
        else:
            return True