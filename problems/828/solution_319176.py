def primo(numero):
    '''A função verifica se o número
    é primo ou não.
    int --> bool'''

    divisores = 0
    counter = 0

    while counter <= numero:
        if counter > 0:
            if numero % counter == 0:
                divisores += 1
        counter += 1

    if divisores == 2:
        return True
    else:
        return False