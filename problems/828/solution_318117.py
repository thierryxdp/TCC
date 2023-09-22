def primo(numero):
    divisores = []
    for i in range(numero):
        if numero%(i+1)==0:
            divisores += [i,]
    return divisores==3