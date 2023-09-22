def fatorial(num):
    '''Recebe um número e retorna o fatorial deste número;
       int -> int'''
    
    mult = 1
    
    for n in range(1,num+1):
        
        mult *= n
        
    return mult