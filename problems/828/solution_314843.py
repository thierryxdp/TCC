def primo (numero):
    '''retorna um valor booleano dizendo se o número dado é primo ou não'''
    '''int -> bool''' 
    
    divisor=1
    
    while divisor < numero:
        if numero%divisor != 0:
            divisor= divisor + 1
            
            return True 
        
        else: 
            return False