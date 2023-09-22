def qtd_divisores(numero):
    '''retorna a quatidade de divisores que o numero dado tem'''
    '''int -> int'''
   
    divisor=1
    
    while divisor <= numero:
        
    x = numero % divisor
    divisor = divisor +1
    
    if x == 0:
        return (divisor-1)