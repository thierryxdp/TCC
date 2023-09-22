def primo (numero):
    '''Funcao que, dado um numero inteiro positivo, retorna se este numero é primo ou não.
    int->bool'''
    
    divisores = 0
    
    for divisor in range(1, numero):
        if numero % divisor == 0:
            divisores = divisores + 1
            if divisores > 1:
                break
    
    if divisores > 1:
        return True
    
    else:
        return False