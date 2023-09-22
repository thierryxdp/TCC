def primo(n):
    '''
    recebe um numero inteiro positivo, retorna True se o 
    numero for primo e false se não for
    int->bool
    '''
    for i in range(2,n):
        if n%i==0:
            return False
    else: 
        return True