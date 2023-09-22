def fatorial(num):
    '''dado umm numero num é retornado a fatorial desse numero
    int---->int'''
    fat = num
    num -= 1
    while(num>0):
        fat = fat*num
        num = num - 1
    return fat