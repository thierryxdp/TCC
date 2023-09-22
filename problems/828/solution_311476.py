def primo(numero):

    divisores=0
    for valor in list(range(1,numero+1)):
        if numero%valor==0:
            x=numero/valor
            divisores=int((x/x)+divisores)
    return divisores