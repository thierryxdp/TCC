def fatorial(n):
    '''função que calcula o numero fatorial dado um numero
    int -> int'''
    fat = 1
    while n > 0:
        fat *= n
        n -= 1
    return fat