def fatorial(n):
    '''Dado um número como entrada, calcula o fatorial desse número.'''
    fat = 1
    i = 0
    while i <= n:
        fat = fat*i
        i = i + 1

    return fat