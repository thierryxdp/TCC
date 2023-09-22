def primo(numero):
    '''retorna se um numero é primo ou nao'''
    '''int -> bool'''
    
    divisor=1
    i=0
    
    
    while divisor<(numero+1):
        if (numero%divisor) == 0:
            i+=1
            divisor+=1
            
            return True
        
        else:
            return False