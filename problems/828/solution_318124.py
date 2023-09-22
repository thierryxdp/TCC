def primo(numero):
    divisores = []
    for i in range(numero+1):
        if numero%(i+1)==0:
            divisores += [i,]
    return divisores==3