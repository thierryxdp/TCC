def primo(numero):
    '''retorna se um numero é primo ou nao'''
    '''int -> bool'''
    
    divisor=1
    
    for divisor in range(1,numero):
        if numero%divisor == 1:
            divisor = divisor+1
            
        return True
        
    else:
        return False