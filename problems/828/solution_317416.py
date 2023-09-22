def primo(numero):
    ''' função que verifica se o número dado é primo
    int -> bool
    '''
    i = 0
    
    for elemento in range(2, numero):
        if numero // elemento == 0:
            i += 1
    if i > 0:
        return False
    else:
        return True