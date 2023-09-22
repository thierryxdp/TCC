def qtd_divisores (n):
    ''' Dado um numero n, retorna quantos divisores esse numero tem'''
    for divisor in range(0, n+1):
        if n % divisor == 0:
            return divisor