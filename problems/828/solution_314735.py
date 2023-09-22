def primo(numero):
    '''Verifica se o numero é positivo ou não
    int->bool'''
    i=2
    while i<numero:
        if i%numero==0:
            return False
        i=i+1
    return True