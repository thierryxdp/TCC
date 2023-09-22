def primo(numero):
    for i in range(numero):
        if i>=2 and numero%i==0:
            return False
        else:
            return True