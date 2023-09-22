def qtd_divisores(numero):
    '''retorna a quatidade de divisores que o numero dado tem'''
    '''int -> int'''
   
    divisor=1
    
    while divisor <= numero:
        
    if (numero % divisor) == 0:
        divisor = divisor +1
        
        return divisor - 1