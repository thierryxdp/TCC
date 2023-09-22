def qtd_divisores(numero):
    '''
    
    '''
    total = 0
    for num in range(1, (numero + 1)):
        if numero % num == 0 and numero > 0:
            total = total + 1
            
    return total