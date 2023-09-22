def fatorial(num):
    '''Recebe um número e retorna o seu fatorial
    int -> int'''
    fat = 1
    while num > 1:
        fat *= (num * (num - 1))
        num -= 2
    return fat