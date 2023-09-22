def qtd_divisores(numero):
    '''
    
    '''
    total = 1
    for num in range(1, numero):
        if numero % num == 0:
            total += 1
        
    return total