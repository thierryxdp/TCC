def qtd_divisores(n):
    '''função que conta e retorna quantos divisores um número tem'''
    i = 0
    for divisor in range(1,n+1):
        if n % divisor == 0:
            i = i + 1
    return i