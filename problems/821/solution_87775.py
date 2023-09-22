def fatorial(n):
    '''Função que recebe um numero e retorna sua fatorial int->int'''
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num