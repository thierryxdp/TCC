def qtd_divisores(numero):
    '''
    
    '''
    total = 0
    for num in range(1, numero//2 + 1):
        if numero % num == 0:
            total += 1
    return total