def fatorial(num):
    fat = num
    num -= 1
    while(num>0):
        fat = fat*num
        num = num - 1
    return fat