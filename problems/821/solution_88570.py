def fatorial(num):
    fat = 0
    while(num>1):
        fat += (num)*(num-1)
        num = num - 1
    return fat