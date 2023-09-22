def primo(n):
    '''função que retorna se um número é primo ou não'''
    '''int-->bool'''
    for i in range(2,n):
        if n%i==0:
            return False
        
    return True