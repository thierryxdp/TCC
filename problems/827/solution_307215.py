def qtd_divisores(numero):
    '''retorna a quatidade de divisores que o numero dado tem'''
    '''int -> int'''
   
    i=1
    
    while i <= numero:
        divisor=numero%i
        i=i+1
        
        if divisor == 0:
            
        return i