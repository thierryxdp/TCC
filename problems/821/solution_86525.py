def fatorial(num):
    ''' Essa função dado um numero, calcula o fatorial deste numero
    int -> int'''
    fat = num
    while num > 1:
        fat = fat * (num - 1)
        num -= 1
    return fat