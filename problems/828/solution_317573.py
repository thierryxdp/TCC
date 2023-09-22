def primo(numero):
    '''
    função que retorna o booleano "True" caso o numero dado como entrada seja primo
    e retorna "False" caso o numero de entrada não seja primo.
    int->bool
    '''
    if numero < 2:
        return False
    else:
        for n in range(2, numero):
            if numero % n == 0:
                return False
        return True