def primo(n):
    '''
    '''
    proximo=0
    divisor=2
    
    for x in range(2,n):
        if range(2,n)[proximo]%divisor==0:
            return True 
        divisor=divisor+1
        proximo=proximo+1
        
    return False