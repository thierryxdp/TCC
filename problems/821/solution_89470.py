def fatorial(num):
    '''função que dado um número, calcule o fatorial deste número'''
    '''int -> complex'''
    while num > 1:
        fat = num * (num - 1)
        num = num - 1
    return fat