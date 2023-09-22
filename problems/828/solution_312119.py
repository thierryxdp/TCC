def primo (numero):
    '''Funcao que, dado um numero inteiro positivo, retorna se este numero é primo ou não.
    int->bool'''
    
    divisores = 0
    
    for divisores in range(1,n+1):
        if n % divisores == 0:
            divisores += 1 
    
    if divisores == 2:
        return True
    
    else:
        return False