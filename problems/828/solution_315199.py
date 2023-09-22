def primo(numero):
    ''''''
    '''int -> bool'''
    
    divisor=2

    while divisor <= numero:
        if numero%divisor != 0:
            divisor=divisor+1
            
        return False
    
    else: 
        if numero%divisor == 0:
            return True