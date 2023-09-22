def primo(numero):
    '''Indica se o numero
    dado e ou nao primo
    int --> bool'''
    qntd = 0
    for i in range (1,numero+1):
        if numero % i == 0:
            qntd = qntd + 1
    if qntd > 2:
        return False
    else:
        return True