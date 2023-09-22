def primo(numero):
    '''retorna se um numero é primo ou nao'''
    '''int -> bool'''
    
    divisor=1
    i=0
    
    
    while divisor<numero:
        if (numero%divisor) == 0:
            i+=1
            divisor+=1
            
            return False
        
        else:
            return True