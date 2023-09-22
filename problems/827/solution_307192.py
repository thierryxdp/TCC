def qtd_divisores(numero):
    '''retorna a quatidade de divisores que o numero dado tem'''
    '''int -> int'''
    
    i=1
    soma=0
    
    while i<=numero:
        
        if numero%i == 0:
            soma=soma+1
            i=i+1
            
        return soma