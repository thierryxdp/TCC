def primo(n):
    '''Função que verifica se o número(n) é primo ou não
    retornando um valor booleano.
    int ->bool'''  
    primos=0
    for i in range(2,n):
        if n%i==0:
            primos=primos+1  
    if primos==0:
        return True
    else:        
        return False