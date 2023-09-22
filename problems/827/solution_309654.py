def qtd_divisores(n):
    '''
    
    '''
    tot = 0
    for num in range(1, (n + 1)):
        if n % num == 0 and n > 0:
            tot = tot + 1
            
    return tot