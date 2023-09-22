def fatorial (x):
    '''Dado um número, retornar o fatorial deste número;
    int -> int'''
    
    i = 0
      
    while x > 0:
        
         x = x + x * i
                    
        i=i+1
        
    return x