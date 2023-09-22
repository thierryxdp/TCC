def fatorial(numero):
    '''Função que dado um número, retorna o fatorial desse numero
    int -> int'''

    
    if numero ==0: 
        return 1
        
    else: 
        fatorial = 1
        while(numero > 1):
            fatorial *= numero
            numero -= 1
            
        return fatorial