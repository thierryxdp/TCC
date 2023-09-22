def primo(n):
    '''
    Recebe um inteiro n e retorna um bool dizendo se n é primo ou não
    
    int -> bool
    '''
    for d in range(2,n):
        if n%d==0:
            return False
    return True