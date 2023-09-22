def fatorial(num):
    '''Recebe um número e retorna o seu fatorial
    int -> int'''
    while num > 1:
        fat += num * (num - 1)
        num -= 1
    return fat