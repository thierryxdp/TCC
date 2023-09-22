def primo (numero):
    '''Funcao que, dado um numero inteiro positivo, retorna se este numero é primo ou não.
    int->bool'''
    
    divisores = 0
    
    for divisor in range(1,n+1):
        if n % divisor == 0:
            cont_divisores += 1 
    
    if cont_divisores == 2:
        return True
    
    else:
        return False