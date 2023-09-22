def qtd_divisores(n):
    '''Esta função conta quantos divisores um numero tem
    int >>> int '''
    qtd = 0
    for i in range(1, n+1):
        if n % i == 0:
            qtd += 1
            
    return qtd