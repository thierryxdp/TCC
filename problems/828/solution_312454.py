def primo(numero):
    """função na qual verifica se o parametro passado e um numero primo ou nao"""
    fator = 2
    while numero % fator != 0 and fator <= numero/2:
        fator += 1
    if numero % fator == 0:
        return False
    else:
        return True