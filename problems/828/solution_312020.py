def primo(numero):
    proximo=2
    while proximo < numero and proximo > 1:
        if numero%proximo==0:
            proximo +=1
        return False
    else:
        return True