def qtd_divisores(numero):
    '''Função que recebe um número e conta quantos divisores ele tem
    
    int->int'''
    
    divisores = 0
    
    for numeros in range(1, numero+1):
        
        if numero%numeros == 0:
            divisores = divisores + 1
            
    return divisores