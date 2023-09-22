def fatorial(n):
    '''função que calcula o fatorial dado um numero n. int ->complex'''
    fat = n
    while n > 1:
        fat = fat * (n - 1)
        n -= 1 
    return fat