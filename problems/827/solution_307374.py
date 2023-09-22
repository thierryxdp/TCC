def qtd_divisores(numero):
    '''retorna a quatidade de divisores que o numero dado tem'''
    '''int -> int'''
   
    divisor=1
    
    for divisor in range(1, numero + 1):
        if numero % divisor == 0:
            divisor=divisor+1
            
        return divisor