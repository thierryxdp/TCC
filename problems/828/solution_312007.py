def primo(numero):
    proximo=2
    for proximo in range(2,numero):
        if numero%proximo==0:
            proximo += 1
        return False