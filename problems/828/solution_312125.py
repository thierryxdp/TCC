def primo (n):
    '''Funcao que, dado um numero inteiro positivo, retorna se este numero é primo ou não.
    int->bool'''
    
    i = 2
    while i <= n/2 and primo:
        if n % i == 0:    
            return False  
        i += 1
    return True