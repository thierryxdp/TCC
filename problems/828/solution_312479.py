def primo(n):
    '''Verifica se um dado número é primo;
    int -> boolean'''
    
    if n == 1 or n == 2:
        return True
    
    elif n == 0:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True