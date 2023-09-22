def primo(numero):
    divisores = []
    for i in range(numero):
        if numero%(i)==0:
            divisores += [i,]
    return len(divisores)==3