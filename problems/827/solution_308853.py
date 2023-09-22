def qtd_divisores(num):
    
    '''
    Nessa função foi verificado quantas vezes podemos dividir o num por um número
    '''
    #int -> int -> int
    
    result = 0
    
    for d in range((1),num+1):
        if num%d == 0:
            result += 1
            
    return result