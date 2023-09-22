def primo(n):
    '''Função que verifica se o número(n) é primo ou não
    retornando um valor booleano.
    int ->bool'''  
    i=0
    for i in range(1,n+1):
        if n%i==0:
            i+=1  
    if i==0:
        return True
    else:        
        return False