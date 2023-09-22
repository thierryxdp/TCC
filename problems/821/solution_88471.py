def fatorial(n):
    '''Função que dado um numero n, calcula e retorna o fatorial desse numero'''
    '''int/float -> int/float'''
    numero = 1
    while n >= 1:
        numero = numero * n
        n -= 1
    return numero