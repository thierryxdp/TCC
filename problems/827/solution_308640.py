def qtd_divisores (n):
    ''' Dado um numero n, retorna quantos divisores esse numero tem'''
    for i in range(0, n/2+1):
        if n % i == 0:
            return i