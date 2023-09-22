def qtd_divisores(numero):
    '''retorna a quatidade de divisores que o numero dado tem'''
    '''int -> int'''
    
    divisor=0
    soma=0
    
    while divisor<=numero :
        if  numero%divisor=0 :
            soma=soma+1
            divisor=divisor+1
            
        return soma