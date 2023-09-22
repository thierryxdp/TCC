def primo(numero):
    for i in range(2,int(numero/2)+1):
        if numero%i==0:
            return False
    return True