def primo(n):
    '''Função que verifica se o número(n) é primo ou não
    retornando um valor booleano.
    int ->bool'''  
    N=0
    for i in range(2,n):
        if n%i==0:
            N=N+1  
    if N==0:
        return True
    else:        
        return False