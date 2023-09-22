def primo(numero):
    ''' '''
    for i in range(2,numero):
        if numero % i==0:
            return False
        else:
            return True