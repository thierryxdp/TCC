def qtd_divisores(numero):
    '''retorna a quatidade de divisores que o numero dado tem'''
    '''int -> int'''
    
    soma=0
   
    for divisor in range(1, numero+1):
        if numero % divisor == 0:
            soma += 1
            
            return soma