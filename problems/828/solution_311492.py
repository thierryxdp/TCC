def primo(x):
    '''funcao que verifica se o numero e primo ou nao. int->bool.'''
    multiplos = 0
    for count in range(2,x):
        if (x % count == 0):
            multiplos += 1
            
    if(multiplos == 0):
        return 'True'
    else:
        return 'False'