def primo(numero):
    for x in range(2,numero):
        if (numero%x==0):
            return bool(False)
        else:
            return bool(True)