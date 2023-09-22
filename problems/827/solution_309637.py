def qtd_divisores(numero):
    '''
    
    '''
    total = 0
    for num in range(1, numero):
        if numero % num == 0 and numero > 0:
            total = total + 2
        
    return total