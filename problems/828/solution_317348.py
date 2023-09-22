def primo(n):
    '''
    Funcao que recebe um numero inteiro. A funcao retorna se o numero e inteiro ou nao.
    int -> bool
    ''' 
    for i in range(2, n):
        if n%i == 0:
            return False
    return True