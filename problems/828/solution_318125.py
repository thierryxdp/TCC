def primo(numero):
    divisores = []
    for i in range(numero+1):
        if numero%(i+1)==0:
            divisores += [i+1,]
    return divisores==3