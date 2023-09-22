def primo(ns):
    '''
    
    '''
    if ns < 2:
        return False
    else:
        for n in range(2, ns):
            if ns % n == 0:
                return False
        return True