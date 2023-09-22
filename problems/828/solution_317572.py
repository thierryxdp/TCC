def primo(numero):
    '''
    
    '''
    if numero < 2:
        return False
    else:
        for n in range(2, numero):
            if numero % n == 0:
                return False
        return True