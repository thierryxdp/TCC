def fatorial(num):
    '''dado um numero, calcula seu fatorial
    int -> int'''
    while num != 1:
        return num * fatorial(num - 1)
    return 1