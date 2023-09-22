def qtd_divisores(numero):
    '''
    
    '''
    total = 0
    for num in range(int, numero):
        if numero % num == 0 and numero > 0:
            total += 1
        
    return total