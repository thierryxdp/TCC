def fatorial(num):
    """ dado um numero calcula seu fatorial"""
    i= 1
    while num > 1:
        i = i*num
        num = num-1
    return i