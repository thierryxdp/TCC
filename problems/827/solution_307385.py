def qtd_divisores(numero):
    '''retorna a quatidade de divisores que o numero dado tem'''
    '''int -> int'''
    
    divisor=1
    soma=0
    
    for divisor in range(1, numero) :
        if  numero%divisor==0 :
            soma=soma+1
            divisor=divisor+1
            
    return soma + 1