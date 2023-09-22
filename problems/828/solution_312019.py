def primo(numero):
    proximo=2
    for proximo in range(2,numero):
        while numero%proximo==0:
            proximo += 1
            return True
        if numero%proximo!=0:
            proximo += 1
            return False