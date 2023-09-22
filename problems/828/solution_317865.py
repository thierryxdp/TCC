def primo(numero):
    i = 0
    for c in range(1,numero+1):
        if (numero % c) == 0:
            i += 1
    if i > 2:
        return False
    else:
        return True