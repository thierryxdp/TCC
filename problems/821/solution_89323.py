def fatorial(num):
    x = num -1
    y = 0
    while 0 < x < num and 0 < num :
        if num > 0:
            y = y + (num * x)
        num = num -2
        x = x-1

    return y