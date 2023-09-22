def qtd_divisores(n):
    '''Função que conta quantos divisores um número tem; int -> int'''
    for i in range(1, n + 1):
        if n % i == 0: