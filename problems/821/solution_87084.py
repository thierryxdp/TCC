def fatorial(num):
    '''funo que dado um numero, calcule o fatorial deste numero'''
    fat = num
    while num > 1:
        fat = fat * (num - 1)
        num -= 1
    return fat