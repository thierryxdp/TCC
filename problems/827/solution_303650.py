def qtd_divisores(n):
    '''dado um numero n, retorna quantos divisores o numero tem
    int->int'''
    divisor = 0
    for i in range(1, n+1):
        if n % i == 0:
            divisor = divisor + 1
    return divisor