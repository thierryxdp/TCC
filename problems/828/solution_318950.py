def primo(numero):
    '''A função verifica se o número
    é primo ou não.
    int --> bool'''
    
    counter = 0
    
    for elemento in range(2, numero):
        if numero % elemento == 0:
            counter += 1
            
    if counter > 0:
        return False
    else:
        return True