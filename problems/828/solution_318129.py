def primo(numero):
    divisores = []
    for i in range(numero):
        if numero%(i+1)==0:
            divisores += [i+1,]
    return len(divisores)==3